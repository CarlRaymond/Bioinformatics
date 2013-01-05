'''
Created on Dec 24, 2012

@author: Carl Raymond
'''

"""Solves the problem of transforming one permutation to another by branch and bound.  The problem
 is transformed to an equivalent one where we transform a permutation to the identity permutation.
 The bounding function is based on the number of breakpoints in a candidate permutation.  This number
 is zero for the identity permutation, which is the motivation for the transformation.

 Permutations are represented by tuples containing integers 1 through n (not 0 through n-1) because that
 matches the problem domain.

 A solution state (a node in the search space) is a triple consisting of a score, a list of pairs
 representing reversals, and tuple representing the permutation that is the result of applying the
 reversals to the starting permutation.
 Example: (6, [(0,2), (3,4)], (10, 8, 6, 4, 5, 1, 2, 4, 3, 7))

 We start by generating a naive solution as the initial best guess and put it into a priority queue ordered
 by the bounding value.
"""

from priorityQueue import PriorityQueue
from sys import exit

def breakpoints(perm):
    """The breakpoint positions in a permutation."""
    n = len(perm)
    if perm[0] != 1:
        yield 0
    for i in range(1, n):
        if abs(perm[i] - perm[i-1]) != 1:
            yield i
    if perm[n-1] != n:
        yield n

def breakpointCount(perm):
    return sum(1 for bp in breakpoints(perm))

def reversalBound(perm):
    """A lower bound on the number of reversals needed to sort a permutation.
       The bound is the ceiling of half the number of breakpoints.  This is a weak bound that
       can be improved later by adding more smartness."""
    return (breakpointCount(perm)+1)/2

def annotatedPerm(perm):
    """A string representation of a permutation with the breakpoints indicated by *"""
    s = []
    n = len(perm)
    lastbp = 0
    for bp in breakpoints(perm):
        for k in xrange(lastbp, bp):
            s.append(str(perm[k]))
        lastbp = bp
        s.append("*")
    for k in xrange(lastbp, n):
        s.append(str(perm[k]))
    return ' '.join(s)

def inverse(perm):
    """Invert a permutation"""
    inv = [0] * len(perm)
    for i, p in enumerate(perm):
        inv[p-1] = i+1
    return tuple(inv)

def compose(a, b):
    """Compose permutations a and b"""
    comp = [0] * len(a)
    for i in xrange(len(a)):
        comp[i] = b[a[i]-1]
    return tuple(comp)

def reverse(perm, (i,j)):
    """Generate elements of a new permutation by applying the reversal indicated by (i,j) to perm"""

    for k in xrange(i):
        yield perm[k]
    for k in xrange(i, j+1):
        yield perm[j+i-k]
    for k in xrange(j+1, len(perm)):
        yield perm[k]
        

   
def applyReversal(incumbent, rev):
    """Apply a reversal to a solution state."""
    score, revlist, perm = incumbent
    newrevlist = list(revlist)
    newrevlist.append(rev)
    newperm = tuple(reverse(perm, rev))
    newscore = len(newrevlist) + reversalBound(newperm)
    return ( newscore, newrevlist , newperm )


def isSolution(incumbent):
    """Compare the resulting permutation in a state to the identity permutation."""
    for pos, val in enumerate(incumbent[2]):
        if val != pos+1: return False
    return True

 
def naiveSolution(perm):
    """Construct the naive solution by putting each element into
       place in turn. This requires at most n-1 reversals."""
    revlist = []
    n = len(perm)
    result = list(perm)
    for i in range(n-1):
        if result[i] != i+1:
            for j in range(i+1, n):
                if result[j] == i+1:
                    result = list(reverse(result, (i,j)))
                    revlist.append((i,j))
    return (len(revlist), revlist, tuple(range(1, n+1)))


def indexOfPerm(queue, perm):
    for pos, state in enumerate(queue):
        if state[2] == perm:
            return pos
    return -1
    

def productiveReversals(perm):
    "Generates reversals to apply to a perm that avoid the ends of the perm if they're in order"
    # Find first and last out-of-place positions
    for left in xrange(len(perm)):
        if perm[left] != left+1: break;
    else: return [] # Fully ordered?
    for right in xrange(len(perm)-1, 0, -1):
        if perm[right] != right+1: break
    return [(i,j) for i in xrange(left, right) for j in xrange(i+1, right+1)]

def breakpointReversals(perm):
    """Reversals to apply to a perm that correspond to the perm's breakpoints"""
    bps = list(breakpoints(perm))
    return [(left, right-1) for left in bps[:-1] for right in bps[1:] if left < right-1]

with open("rosalind_rear.txt") as spec:
    start = tuple([int(x) for x in spec.readline().split()])
    goal = tuple([int(x) for x in spec.readline().split()])

#start = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
#goal = [ 3, 1, 5, 2, 7, 4, 9, 6, 10, 8 ]
n = len(goal)

print "Start: ", annotatedPerm(start)
print "Goal: ", annotatedPerm(goal)
print "Inverse goal: ", inverse(goal)

# Transforming start to goal is the same as transforming alpha to the identity
# permutation. (Look it up!)
alpha = compose(start, inverse(goal))
print "Alpha: ", annotatedPerm(alpha)

# The initial best solution is the naive solution.
bestState = naiveSolution(alpha)
bestScore = bestState[0]
print "Naive solution: ", bestState
acceptCount = 0
rejectCount = 0

# Representation of a solution incumbent is a triple (score, revlist, result) where
# revlist is a list of reversals, result is the permutation after applying the
# reversals to the starting permutation, and score is the length of revlist
# plus the reversalBound of the result.
initialState = (reversalBound(alpha), [], alpha)
print "Initial state: ", initialState

# Build a list of all possible reversals.
allrevs = [(i,j) for i in xrange(n-1) for j in xrange(i+1, n)]

# The queue is implemented as a list of dictionaries. Each dictionary holds items of
# the same score (0...n-1).
queue = PriorityQueue(n)
queue.insert(initialState)
maxQueueLen = len(queue)

while True:
    l = len(queue)
    if l % 1000 <= 5:
        print l
        
    incumbent = queue.pop()
    if incumbent == None: break
    
    #print "Popping ", incumbent
    if (incumbent[0] >= bestScore):
        #print "Rejecting ", incumbent
        continue

    if isSolution(incumbent):
        print "Found new best: ", incumbent
        bestScore = incumbent[0]
        bestState = incumbent
        continue
    
    for r in breakpointReversals(incumbent[2]) :
        newstate = applyReversal(incumbent, r)
        if newstate[0] < bestScore: 
            acceptCount += 1
            queue.insertUnlessPresent(newstate)
        else:
            rejectCount += 1
            #print "Rejecting ", newstate
    maxQueueLen = max(maxQueueLen, len(queue))
    
    
print  "Best: ", bestState

# Validate the result
print "Start:  ", start
perm = list(start)
for rev in bestState[1]:
    perm = list(reverse(perm, rev))
    print rev, ":", perm

if tuple(perm) == goal:
    print "Validated!"
else:
    print "Oops! Something went wrong."

print "Accepted: {0:,}".format(acceptCount)
print "Rejected: {0:,}".format(rejectCount)
print "Maximum queue length: {0:,}".format(maxQueueLen)

print
print len(bestState[1])
for (i,j) in bestState[1]:
    print i+1, j+1