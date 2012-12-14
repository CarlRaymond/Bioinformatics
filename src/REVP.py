complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
minl = 4;
maxl = 12;

def checkrevp(seq, compseq, start, span):
    for i in xrange(span):
        if seq[start+i] != compseq[start+span-i]:
            return False
    return True

with open("rosalind_revp.txt") as input:
    with open("rosalind_revp.out", "w+") as output:
        seq = input.readline().strip()
        compseq = "".join(complement[base] for base in seq);
        length = len(seq)
        for start in xrange(length-minl+1):
            for span in xrange(minl-1, min(maxl, length-start)):
                if checkrevp(seq, compseq, start, span):
                    output.write("{0} {1}\n".format(start+1, span+1))

raw_input()





