'''
Created on Jan 8, 2013

@author: Carl Raymond
'''

with open("rosalind_kmp.txt") as spec:
    seq = spec.readline().strip()

#print seq

n = len(seq)
print "Length:", n

failure = [0] * n
#failure[0] = 0

m = 0
k = 1
while k<n:
    if seq[k] == seq[m]:
        m += 1
        failure[k] = m
        k += 1
    elif m > 0:
        m = failure[m]
        print "Backtrack at", k
    else:
        failure[k] = 0
        m = 0
        k += 1

print "Failure:"        
for f in failure: print f,
print
        