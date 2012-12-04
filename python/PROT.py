codons = {
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
'UAA': None, 
'UAG': None,    
'UGU': 'C',        
'UGC': 'C',        
'UGA': None,
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


with open("rosalind_prot.txt") as input:
    dna = input.readline().strip();
    print "dna: ", dna
    p = [];
    for i in range(0, len(dna), 3):
        c = dna[i:i+3];
        a = codons[c];
        if a: p.append(a);
        print " codon: ", c;
    protein = "".join(p);
    print protein

with open("rosalind_prot.out", "w+") as output:
    output.write(protein);

raw_input()
