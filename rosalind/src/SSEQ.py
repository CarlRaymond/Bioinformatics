'''
Created on Jan 27, 2013

@author: Carl Raymond
'''

with open("rosalind_sseq.txt") as spec:
    seq = spec.readline().strip()
    subseq = spec.readline().strip()

print seq
print subseq

pos = 0
n = len(seq)
for c in subseq:
    pos = seq.index(c, pos)+1
    print pos,
    
        