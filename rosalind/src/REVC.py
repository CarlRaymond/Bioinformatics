baseComplement = { 'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A' }

def revc(seq):
    return "".join([baseComplement[base] for base in seq[::-1]])

if __name__ == '__main__':
    with open("rosalind_revc.txt") as data, open("rosalind_revc.out", mode="w+") as output:
        for seq in data:
            seq = seq.strip()
            output.write(revc(seq))
            output.write('\n')