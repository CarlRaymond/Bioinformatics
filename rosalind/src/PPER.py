'''
Created on Dec 23, 2012

@author: Carl Raymond
'''

with open("rosalind_pper.txt") as spec:
    n, k = [int(x) for x in spec.readline().split()]

print n, k

perm = 1
for i in range(n, n-k, -1):
    perm = (perm * i) % 1000000
    
print perm
