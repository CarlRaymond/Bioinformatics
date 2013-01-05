'''
Created on Jan 3, 2013

@author: Carl Raymond
'''
from itertools import chain
from codons import splitCodons
from codons import proteinFromCodons

with open("rosalind_splc.txt") as spec:
    seq = spec.readline().strip()
    exons = [exon.strip() for exon in spec]
    
print "Seq (len {0}):".format(len(seq)), seq
print exons

introns = [ seq ]
print introns
for ex in exons:
    sp = [intr.split(ex) for intr in introns]
    introns = list(chain.from_iterable((sp)))
    print introns

dna = "".join(introns)
print "DNA: ", dna

# Convert DNA to RNA
rna = dna.replace('T', 'U')
print "RNA: ", rna

codons = splitCodons(rna)
protein = proteinFromCodons(codons)

print
print protein[:-1]