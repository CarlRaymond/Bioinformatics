'''
Created on Dec 14, 2012

@author: carl
'''
import string

codonTable = {
'UUU': 'F',        
'UUC': 'F',       
'UUA': 'L',       
'UUG': 'L',       
'UCU': 'S',       
'UCC': 'S',       
'UCA': 'S',       
'UCG': 'S',       
'UAU': 'Y',       
'UAC': 'Y',
'UAA': '.',
'UAG': '.',     
'UGU': 'C',        
'UGC': 'C',
'UGA': '.',        
'UGG': 'W',        
'CUU': 'L', 
'CUC': 'L', 
'CUA': 'L', 
'CUG': 'L', 
'CCU': 'P', 
'CCC': 'P', 
'CCA': 'P', 
'CCG': 'P', 
'CAU': 'H', 
'CAC': 'H', 
'CAA': 'Q', 
'CAG': 'Q', 
'CGU': 'R', 
'CGC': 'R', 
'CGA': 'R', 
'CGG': 'R',  
'AUU': 'I',  
'AUC': 'I',  
'AUA': 'I',  
'AUG': 'M',  
'ACU': 'T',  
'ACC': 'T',  
'ACA': 'T',  
'ACG': 'T',  
'AAU': 'N',  
'AAC': 'N',  
'AAA': 'K',  
'AAG': 'K',  
'AGU': 'S',  
'AGC': 'S',  
'AGA': 'R',  
'AGG': 'R',  
'GUU': 'V',
'GUC': 'V',
'GUA': 'V',
'GUG': 'V',
'GCU': 'A',
'GCC': 'A',
'GCA': 'A',
'GCG': 'A',
'GAU': 'D',
'GAC': 'D',
'GAA': 'E',
'GAG': 'E',
'GGU': 'G',
'GGC': 'G',
'GGA': 'G',
'GGG': 'G'
};

startCodons = [ 'AUG' ]

stopCodons = [ 'UAG', 'UGA', 'UAA' ]

def isStartCodon(codon):
    return startCodons.__contains__(codon)

def isStopCodon(codon):
    return stopCodons.__contains__(codon)

def splitCodons(seq, start=0):
    limit = len(seq) - start
    limit -= limit % 3
    for i in xrange(start, limit, 3):
        yield seq[i:i+3]

def proteinFromCodons(codons):
    return "".join([codonTable[c] for c in codons])