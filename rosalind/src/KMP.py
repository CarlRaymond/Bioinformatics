'''
Created on Jan 8, 2013

@author: Carl Raymond
'''

from fasta import read

with open("rosalind_kmp.txt") as spec:
    name,seq = read(spec).next()

n = len(seq)
print "Length:", n

failure = [0] * n
#failure[0] = 0

# No. of matches seen so far
m = 0

k = 1
while k<n:
    if seq[k] == seq[m]:
        m += 1
        failure[k] = m
        k += 1
    elif m > 0:
        #print "Backtrack at {0} where m = {1}".format(k, m);
        m = failure[m-1]
        #print "New m = {0}".format(m);
    else:
        failure[k] = 0
        k += 1

with open("rosalind_kmp.out", "w+") as result:
    for f in failure:
        result.write("{0} ".format(f));

        