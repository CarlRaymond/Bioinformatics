with open("rosalind_revc.txt") as input, open("rosalind_revc.out", mode="w+") as output:
    for line in input:
        for n in line[::-1]:
            if n == 'A':
                output.write('T');
            elif n == 'C':
                output.write('G');
            elif n == 'G':
                output.write('C');
            elif n == 'T':
                output.write('A');
