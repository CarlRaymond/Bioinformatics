'''
Created on Dec 25, 2012

@author: Carl Raymond
'''

from itertools import permutations
from math import pow

def factorial(n):
    if n<1: return 1
    return factorial(n-1)*n

def flipSign(l, n, pos):
    if pos < n:
        l[pos] = -l[pos]
        for v in flipSign(l, n, pos+1): yield v
        l[pos] = -l[pos]
        for v in flipSign(l, n, pos+1): yield v
    else:
        yield l

with open("rosalind_sign.txt") as spec:
    n = int(spec.readline())
    

count = int(factorial(n) * pow(2,n))
print count

for p in permutations(range(1,n+1)):
    for x in flipSign(list(p), n, 0):
        for e in x: print e,
        print
    
