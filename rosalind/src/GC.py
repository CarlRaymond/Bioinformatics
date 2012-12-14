import fasta;

def gc(seq):
    gc = 0;
    length = 0;
    for n in seq:
        if (n == 'A' or n == 'T'):
            length += 1;
        elif (n == 'C' or n == 'G'):
            length += 1;
            gc += 1;
    return 100.0 * float(gc) / float(length);

def analyze(sequences):
    for seq in sequences:
        yield (seq[0], gc(seq[1])); 

def maxgc(seq1, seq2):
    return seq1 if (seq1[1] > seq2[1]) else seq2;

with open("rosalind_gc.txt") as data:
    result = reduce(maxgc, analyze(fasta.read(data)));
    print result[0]
    print "{0:4f}%".format(result[1]); 


raw_input();