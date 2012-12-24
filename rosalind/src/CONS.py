'''
Created on Dec 24, 2012

@author: Carl Raymond
'''

from operator import itemgetter

# Returns a dictionary containing counts for each
# base in position pos of the sequences in data.
def consensus(data, pos):
    cons = { 'A':0, 'C':0, 'G':0, 'T':0 }
    for seq in data:
        b = seq[pos]
        cons[b] += 1
    return cons
    
with open("rosalind_cons.txt") as spec:
    data = [seq.strip() for seq in spec]
    
size = len(data[0])
print "{0} sequences of length {1}".format(len(data), size)

consvector = [consensus(data, k) for k in range(size)]

consseq = [max(cons.items(), key=lambda (k,v): v)[0] for cons in consvector]
print "".join(consseq)

print 'A:',
vec = [consvector[k]['A'] for k in range(size)]
for n in vec: print n,
print

print 'C:',
vec = [consvector[k]['C'] for k in range(size)]
for n in vec: print n,
print

print 'G:',
vec = [consvector[k]['G'] for k in range(size)]
for n in vec: print n,
print

print 'T:',
vec = [consvector[k]['T'] for k in range(size)]
for n in vec: print n,
print

