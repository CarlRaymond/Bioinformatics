'''
Created on Nov. 13, 2015

@author: Carl Raymond
'''

'''
Months to iterate
n = 6

Months rabbits live
m = 3

p0		p1		p2
  1		  0		  0
  0		  1		  0
  1			0		  1
  1		  1		  0
  1		  1		  1
  2		  1		  1

'''


with open("rosalind_fibd.txt") as spec:
    line = spec.readline().split();
    n = int(line[0]);
    m = int(line[1]);

population = [0] * m
population[0] = 1

for i in xrange(n-1):
	# No. of new rabbits is sum of rabbits one month or older
	babies = sum(population) - population[0]
	# Shift rabbits up one month in age
	population.pop()
	population.insert(0, babies)
	print population

total = sum(population)

print total
