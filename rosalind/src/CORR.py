'''
Created on Dec 23, 2012

@author: Carl Raymond
'''

from REVC import revc
from fasta import read

# Returns true when the Hamming distance between seq1 and seq2
# is exactly n.  Faster than computing the distance first when
# we're only interested in small distances.
def isDistance(seq1, seq2, n):
    dist = 0
    for (c1, c2) in zip(seq1, seq2):
        if c1 != c2:
            dist += 1
            if (dist > n): return False
    return dist == n


with open("rosalind_corr.txt") as spec:
    rawdata = [seq.strip() for name,seq in read(spec)]
    

# Build a dictionary with reads as keys and counts as the value.    
reads = {}
for seq in rawdata:
    if seq in reads:
        reads[seq] += 1
    else:
        reads[seq] = 1
 
print "Original data: {0} sequences.".format(len(rawdata))
print "Distinct reads: {0} sequences.".format(len(reads))   

readsum = sum(v for k,v in reads.iteritems())
print "Total multiplicity: {0}".format(readsum)                                                                                                                             

# Goodreads are have multiplicity > 1 or are present in revc form
goodreads = [seq for seq,mult in reads.iteritems() if mult > 1 or revc(seq) in reads]
print "Good reads: {0}".format(len(goodreads))

# Build list of sequences appearing once
singletons = [seq for seq,mult in reads.iteritems() if mult == 1]
print "Singletons: {0}".format(len(singletons))

#for s in singletons: print s

#for k,v in reads.iteritems():
#    if v > 1: print k,v

# Build list of sequences whose revc was not read  
badreads = [seq for seq in singletons if revc(seq) not in goodreads]

print "Bad reads: {0}".format(len(badreads))

# A bad read must have distance 1 to exactly one good read
with open("rosalind_corr.out", "w+") as output:
    for b in badreads:
        count = 0
        for r in goodreads:
            if isDistance(b, r, 1):
                match = r
                count += 1
            elif isDistance(b, revc(r), 1):
                match = revc(r)
                count += 1

        if count == 1:
            output.write("{0}->{1}\n".format(b, match))
