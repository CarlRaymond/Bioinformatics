'''
Created on Dec 21, 2012

@author: Carl Raymond
'''

from operator import itemgetter

def longestOverlap(head, tail):
    maxlen = min(len(head), len(tail))
    for n in xrange(maxlen, 0, -1):
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

overlap = [[longestOverlap(data[hindex], data[tindex]) if hindex != tindex else None for tindex in xrange(count)] for hindex in xrange(count) ]

print "Overlaps:"
for row in overlap: print row

# Find starting point: choose the sequence that's the worst follower, by having the minimum of maximum overlap when it's the tail
transposed = [[row[i] for row in overlap] for i in xrange(count)]

maxfollow = [max(row) for row in transposed]
index, score = min(enumerate(maxfollow), key=itemgetter(1))
print " 0: {0} ({1})".format(index, score)

superstring = [x for x in data[index]]

# Find each successor 
for n in xrange(count-1):
    nextindex, score = max(enumerate(overlap[index]), key=itemgetter(1))
    print "{0:2}: {1} ({2})".format(n+1, nextindex, score)
    superstring.append(data[nextindex][score:])
    index = nextindex
    
    
result = "".join(superstring)
print "Result:"
print result
print "Total length: {0}".format(len(result))

