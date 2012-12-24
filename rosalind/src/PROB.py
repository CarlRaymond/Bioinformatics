'''
Created on Dec 24, 2012

@author: Carl Raymond
'''
from math import log10

with open("rosalind_prob.txt") as spec:
    seq = spec.readline().strip()
    gcvalues = [float(x) for x in spec.readline().split()]
    
print seq
print gcvalues

for gcval in gcvalues:
    gc = log10(gcval/2)
    at = log10((1-gcval)/2)
    logp = { 'A': at, 'C': gc, 'G': gc, 'T': at}
    
    logprob = sum([logp[b] for b in seq])
    print logprob,