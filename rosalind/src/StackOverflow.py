'''
Created on Jan 12, 2013

@author: Carl Raymond
'''

from suffix_tree import GeneralisedSuffixTree
from random import choice

baseComplement = { 'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A' }

def revc(seq):
    return "".join([baseComplement[base] for base in seq[::-1]])


# Build a random string, which should have some short reverse complements already.
bases = ['A', 'C', 'G', 'T']
data = ''.join(choice(bases) for i in xrange(400000)) 
#data = "AGGGTTTCCCTGACCTTCACTGCAGGTCATGCA"
# revc  TGCATGACCTGCAGTGAAGGTCAGGGAAACCCT
#       012345678901234567890123456789012
#                 1         2         3

print "Got data"
revdata = revc(data)
print "Got reverse data"

n = len(data)
minlength = 18
tree = GeneralisedSuffixTree([data, revdata])
for shared in tree.sharedSubstrings(minlength):
    _, start, stop = shared[0]
    seq = data[start:stop]
    _, rstart, rstop = shared[1]
    rseq = data[n-rstop:n-rstart]
    print "Match: {0} at [{1}:{2}] and {3} at [{4}:{5}]".format(seq, start, stop, rseq, n-rstop, n-rstart)

