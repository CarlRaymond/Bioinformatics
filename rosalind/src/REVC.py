with open("rosalind_revc.txt") as data, open("rosalind_revc.out", mode="w+") as output:
    for line in data:
        for n in line[::-1]:
            if n == 'A':
                output.write('T');
            elif n == 'C':
                output.write('G');
            elif n == 'G':
                output.write('C');
            elif n == 'T':
                output.write('A');
