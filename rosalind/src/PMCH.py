'''
Created on Nov. 21, 2015

@author: Carl Raymond
'''

from fasta import read
from math import factorial

with open("rosalind_pmch.txt") as spec:
    name,seq = read(spec).next()

count = { 'A': 0, 'U': 0, 'C': 0, 'G': 0 }

# Count each nucleotide
for n in seq:
    count[n] += 1

# Validate counts
assert count['A'] == count['U'], "No. of A nucleotides is {0}, no. of U nucleotides is {1}. Bad.".format(count['A'], count['U'])

print count

# No. of perfect matchings is a! * c!
matchings = factorial(count['A']) * factorial(count['C'])

print "Matchings: {0}".format(matchings)
