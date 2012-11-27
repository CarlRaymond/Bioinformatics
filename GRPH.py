import fasta;


nodes = [];
with open("rosalind_grph.txt") as input:
    for node in fasta.read(input): nodes.append(node);

with open("rosalind_grph.out", "w+") as output:
    for (l, r) in [(l, r) for l in nodes for r in nodes if l != r and l[1][-3:] == r[1][:3] ]:
        output.write("{0} {1}\n".format(l[0], r[0]));

#raw_input()