'''
Created on Jan 7, 2013

@author: Carl Raymond
'''

from fasta import read

with open("rosalind_kmer.txt") as spec:
    name, seq = read(spec).next()

counts = {}
dna = "ACGT"
all = [ a+b+c+d for a in dna for b in dna for c in dna for d in dna]
for kmer in all:
    counts[kmer] = 0

n = len(seq)
for k in xrange(n-4+1):
    kmer = seq[k:k+4]
    counts[kmer]+=1

for kmer in all:
    print counts[kmer],