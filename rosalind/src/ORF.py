'''
Created on Dec 14, 2012

@author: carl
'''

import REVC;
import codons;
import string;
import re;

if __name__ == '__main__':
    pattern = r'(?=(M[^\.]*\.))'
    
    with open("rosalind_orf.txt") as spec:
        dna = spec.readline().strip()
        #dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
        print dna
        rna = string.replace(dna, 'T', 'U')
        result = {}
        trans = codons.proteinFromCodons(codons.splitCodons(rna))
        for p in [match.group(1)[:-1] for match in re.finditer(pattern, trans)]:
            result[p] = 1

        trans = codons.proteinFromCodons(codons.splitCodons(rna, 1))
        for p in [match.group(1)[:-1] for match in re.finditer(pattern, trans)]:
            result[p] = 1
        
        trans = codons.proteinFromCodons(codons.splitCodons(rna, 2))
        for p in [match.group(1)[:-1] for match in re.finditer(pattern, trans)]:
            result[p] = 1
        
        rna = string.replace(REVC.revc(dna), 'T', 'U')
        trans = codons.proteinFromCodons(codons.splitCodons(rna))
        for p in [match.group(1)[:-1] for match in re.finditer(pattern, trans)]:
            result[p] = 1
        
        trans = codons.proteinFromCodons(codons.splitCodons(rna, 1))
        for p in [match.group(1)[:-1] for match in re.finditer(pattern, trans)]:
            result[p] = 1
        
        trans = codons.proteinFromCodons(codons.splitCodons(rna, 2))
        for p in [match.group(1)[:-1] for match in re.finditer(pattern, trans)]:
            result[p] = 1

        for r in result.keys(): print r
        