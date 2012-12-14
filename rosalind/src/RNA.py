with open("rosalind_rna.txt") as data:
    with open("rosalind_rna.out", mode="w+") as output:
        for line in data:
            output.write(line.replace("T", "U"));
