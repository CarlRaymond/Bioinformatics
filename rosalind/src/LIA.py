'''
Created on Dec 18, 2012

@author: Carl Raymond
'''
import math

from operator import mul    # or mul=lambda x,y:x*y

nCk = lambda n,k: int(round(
    reduce(mul, (float(n-i)/(i+1) for i in range(k)), 1)))

with open("rosalind_lia.txt") as spec:
    line = spec.readline().split()
    k = int(line[0])
    N = int(line[1])


print "k:", k
print "N:", N

S = pow(2, k)
p = 0.25
q = 1-p
result = sum(nCk(S, i) * pow(p,i) * pow(q, S-i) for i in range(N, S+1))
    
print "Result:", result 