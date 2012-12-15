'''
Created on Dec 13, 2012

@author: Carl Raymond
'''

import itertools;

with open("rosalind_lexf.txt") as spec:
    alphabet = spec.readline().split();
    size = int( spec.readline());
    print alphabet
    print size
    
with open("rosalind_lexf.out", "w+") as output:
    for perm in itertools.product(alphabet, repeat=size):
        output.write("{}\n".format("".join(perm)))
