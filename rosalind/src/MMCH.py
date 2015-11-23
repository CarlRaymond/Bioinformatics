from fasta import read
import math

with open("rosalind_mmch.txt") as spec:
    name,seq = read(spec).next()

count = { 'A': 0, 'U': 0, 'C': 0, 'G': 0 }

# Count each nucleotide
for n in seq:
    count[n] += 1

print count

au_max = max(count['A'], count['U'])
au_min = min(count['A'], count['U'])
cg_max = max(count['C'], count['G'])
cg_min = min(count['C'], count['G'])

print "AU: max: {0},  min: {1}".format(au_max, au_min) 
print "CG: max: {0},  min: {1}".format(cg_max, cg_min)

# A and U can be mapped in au_max! / (au_max - au_min)!
# C and G can be mapped in cg_max! / (cg_max - cg_min)!
au_matches = math.factorial(au_max) / math.factorial(au_max - au_min)
cg_matches = math.factorial(cg_max) / math.factorial(cg_max - cg_min)

print "au_maps: {0}, cg_maps: {1}".format(au_matches, cg_matches)

total = au_matches * cg_matches
print "Total matchings: {0}".format(total)
