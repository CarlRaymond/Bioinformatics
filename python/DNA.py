a = c = g = t = 0;
with open("rosalind_dna.txt") as f:
    for line in f:
        for n in line:
            if n == 'A':
                a += 1;
            elif n == 'C':
                c += 1;
            elif n == 'G':
                g += 1;
            elif n == 'T':
                t += 1;

print a, c, g, t


