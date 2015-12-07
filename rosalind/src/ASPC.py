'''
Created Dec. 6 2015
@author Carl J. Raymond
'''

from math import factorial

with open("data/rosalind_aspc.txt") as spec:
	n, m = [int(x) for x in spec.readline().split()]

sum = 0
for k in xrange(m, n+1):
	sum += factorial(n) / factorial(k) / factorial (n-k)
	 
print n, m
print "Result: ", sum