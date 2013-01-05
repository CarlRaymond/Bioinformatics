'''
Created on Jan 5, 2013

@author: Carl Raymond
'''

from fasta import read

def pdist(seq1, seq2):
    n = min(len(seq1), len(seq2))
    return float(sum( 1 if b1 !=b2 else 0 for (b1, b2) in zip(seq1, seq2))) / n
        
    
with open("rosalind_pdst.txt") as spec:
    data = [ seq for seq in read(spec)]
    
print data
    
n = len(data)
seqlen = len(data[0][1])

dist = [ [ pdist(seq1, seq2) for name2, seq2 in data ] for name1, seq1 in data]

for row in dist:
    for elem in row: print elem,
    print

