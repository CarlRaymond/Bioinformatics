def cost(pair):
    if pair[0] != pair[1]:
        return 1;
    return 0;

def hamming(seq1, seq2):
    return sum(map(cost, zip(seq1, seq2)));

with open("rosalind_hamm.txt") as data:
    seq1 = data.readline().strip();
    seq2 = data.readline().strip();
    print hamming(seq1, seq2);

raw_input();
