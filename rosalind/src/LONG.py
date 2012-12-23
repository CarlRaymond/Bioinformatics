'''
Created on Dec 21, 2012

@author: Carl Raymond
'''

from operator import itemgetter

def maxOverlap(head, tail):
    maxoverlap = min(len(head), len(tail))
    for n in xrange(maxoverlap, 0, -1):
        if head[-n:] == tail[:n]:
            return n
    return 0

# Simple greedy algorithm for finding shortest superstring. May not work in the general
# case.  The starting point is the sequence which is the worst follower (having minimum maxoverlap compared to
# the others as heads when it is the tail).  Then find the successor, which is the sequence with the most overlap.
# Continue finding the best successor, and hope we don't get a cycle.  (Hypothesis: the "overlap by more than
# half" condition will prevent a cycle.)
with open('rosalind_long.txt') as spec:
    data = [seq.strip() for seq in spec]
count = len(data)
print "{0} sequences.".format(count)

# Compute overlap of all pairs.  Omit self-comparisons. overlap[i][j] contains the maximum overlap
# between head sequence i and tail sequence j
overlap = [[ None if h == t else maxOverlap(data[h], data[t]) for t in xrange(count)] for h in xrange(count) ]

print "Overlaps:"
for row in overlap: print row

# Find starting point: choose the sequence that's the worst follower, by having the minimum of maximum
# overlaps with other sequences when it's the tail
# Build list of max follow scores for each sequence
maxfollow = [reduce(max, (row[i] for row in overlap)) for i in xrange(count)]
print maxfollow
# Find the index of the worst follower. It is  the leader.
index, score = min(enumerate(maxfollow), key=itemgetter(1))
print " 0: {0:2} ({1:3})".format(index, score)

# Build the superstring as a list
superstring = [x for x in data[index]]

# Find each successor, which has the most overlap with the previous sequence
for n in xrange(count-1):
    nextindex, score = max(enumerate(overlap[index]), key=itemgetter(1))
    print "{0:2}: {1:2} ({2:3})".format(n+1, nextindex, score)
    superstring.append(data[nextindex][score:])
    index = nextindex
    
    
result = "".join(superstring)
print "Result:"
print result
print "Total length: {0}".format(len(result))
