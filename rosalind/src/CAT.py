'''
Created Nov. 27, 2015
@author Carl J. Raymond
'''

from fasta import read

baseComp = {
	'A' : 'U',
	'C' : 'G',
	'G' : 'C',
	'U' : 'A'
}

# The cache stores computed values of perfectMatchCount, using a key which is
# a tuple (start, stop).
cache = { }
cacheHits = 0

# Computes the number of perfect matchings in seq from position start (incl.)
# to stop (excl.) Uses a cache for much more fastness.
def perfectMatchCount(seq, start, stop):
	global cacheHits
	
	# Check the cache
	if (start, stop) in cache:
		cacheHits += 1
		return cache[(start, stop)]
	
	# An empty interval has a single match consisting of no edges.
	if start >= stop:
		return 1

	# Count matchings by using the start position as the anchor, iterating all
	# possible matching edges between the anchor and its complements, and recursively
	# computing the possible matchings on either side of the edge. Sum the result
	# over all choices of the matching edge.
	anchor = seq[start]
	sum = 0

	# Match anchor will all possible complements in the interval
	for matchPos in [k for k in xrange(start, stop) if seq[k] == baseComp[anchor]]:
		# Count matchings of subgraphs on either side of the edge (start, matchPos)
		left = perfectMatchCount(seq, start+1, matchPos)
		right = perfectMatchCount(seq, matchPos+1, stop)
		sum += left * right
	
	# Cache the result
	cache[(start, stop)] = sum
	
	return sum


with open("data/rosalind_cat.txt") as spec:
    name,seq = read(spec).next()

# Verify that count of A matches count of U, and likewise for C and G.
counts = { 'A': 0, 'C': 0, 'G': 0, 'U': 0 }
for b in seq:
	counts[b] += 1
print "Counts: ", counts

print seq
print perfectMatchCount(seq, 0, len(seq))

print "Cache size: ", len(cache)
print "Cache hits: ", cacheHits