'''
Created on Jan 4, 2013

@author: Carl Raymond
'''

from fasta import read

complements = { 'A': 'G', 'C': 'T', 'G': 'A', 'T': 'C'}

with open("rosalind_tran.txt") as spec:
    reader = read(spec)
    seq1 = reader.next()[1]
    seq2 = reader.next()[1]

ts = 0
tv = 0

for (b1, b2) in zip(seq1, seq2):
    if b1 == b2:
        pass
    elif b1 == complements[b2]:
        ts += 1
    else:
        tv += 1
        
print "Transitions: {0}".format(ts)
print "Transversions: {0}".format(tv)
print "Ratio: {0:5}".format(float(ts) / tv)