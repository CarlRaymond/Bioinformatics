import math

with open("rosalind_rstr.txt") as spec:
    line = spec.readline().split()
    n = float(line[0])
    gcx = float(line[1])
    seq = spec.readline().strip()

atx = 1.0 - gcx
probs = { 'A': atx/2, 'C': gcx/2, 'G': gcx/2, 'T': atx/2 }

print probs

p_match = 1.0
for b in seq:
	p_match *= probs[b]

print p_match

lnp_mismatch = math.log(1.0 - p_match)
lnp_fail = lnp_mismatch * n
p_fail = math.exp(lnp_fail)

p_success = 1.0 - p_fail
print "Probability of one or more matches: {0}".format(p_success)

