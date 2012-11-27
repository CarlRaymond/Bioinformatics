with open("rosalind_rna.txt") as input:
    with open("rosalind_rna.out", mode="w+") as output:
        for line in input:
            output.write(line.replace("T", "U"));
