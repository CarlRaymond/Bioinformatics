'''
Created on Aug 15, 2013

@author: Carl Raymond
'''

'''
Newborn    Repro
1            0
0            1
3            1
3            4
12           7
21					19

'''


with open("rosalind_fib.txt") as spec:
    line = spec.readline().split();
    n = int(line[0]);
    k = int(line[1]);

newborn = 1
repro = 0

for i in xrange(n):
	r2 = newborn + repro
	n2 = repro * k
	repro = r2
	newborn = n2

print "{0}".format(repro)
