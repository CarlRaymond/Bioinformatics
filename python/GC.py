import fasta;

def gc(seq):
    gc = 0;
    len = 0;
    for n in seq:
        if (n == 'A' or n == 'T'):
            len += 1;
        elif (n == 'C' or n == 'G'):
            len += 1;
            gc += 1;
    return 100.0 * float(gc) / float(len);

def analyze(sequences):
    for seq in sequences:
        yield (seq[0], gc(seq[1])); 

def maxgc(seq1, seq2):
    return seq1 if (seq1[1] > seq2[1]) else seq2;

with open("rosalind_gc.txt") as input:
    result = reduce(maxgc, analyze(fasta.fasta(input)));
    print result[0]
    print "{0:4f}%".format(result[1]); 


raw_input();