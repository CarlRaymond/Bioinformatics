'''
Created on Dec 23, 2012

@author: Carl Raymond
'''

from codons import codonTable, startCodons, stopCodons

with open("rosalind_mrna.txt") as spec:
    seq = spec.readline().strip()

# Invert the codon dictionary, where the key is the amino acid, and the
# value is the number of triples coding for that acid.

aacounts = {}
for k,v in codonTable.iteritems():
    if v in aacounts:
        aacounts[v]+=1
    else :
        aacounts[v]=1

# Append stop codon
seq = seq + '.'

ways = 1
for aa in seq:
    ways = ways * aacounts[aa] % 1000000

print ways


