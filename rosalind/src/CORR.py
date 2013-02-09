'''
Created on Dec 23, 2012

@author: Carl Raymond
'''

from REVC import revc

# Returns true when the Hamming distance between seq1 and seq2
# is exactly n.  Faster than computing the distance first when
# we're only interested in small distances.
def isDistance(seq1, seq2, n):
    dist = 0
    for (c1, c2) in zip(seq1, seq2):
        if c1 != c2:
            dist += 1
            if (dist > n): return False
    return dist == n

if __name__ == '__main__':
    with open("corr.txt") as spec:
        rawdata = [seq.strip() for seq in spec]

    # Build a dictionary with reads as keys and counts as the value.    
    reads = {}
    for seq in rawdata:
        if seq in reads:
            reads[seq] += 1
        else:
            reads[seq] = 1
    
    print "Original data: {0} sequences.".format(len(rawdata))
    print "Distinct reads: {0} sequences.".format(len(reads))

    # Build list of sequences appearing once
    singletons = [k for k,v in reads.iteritems() if v == 1]
    print "Singletons: {0}".format(len(singletons))

    for k,v in reads.iteritems():
        if v > 1: print k,v
        
    # Build list of sequences whose revc was not read    
    badreads = [seq for seq in singletons if revc(seq) not in reads]
    print "Bad reads: {0}".format(len(badreads))

    with open("rosalind_corr.out", "w+") as output:
        for b in badreads:
            for r in reads:
                if isDistance(b, r, 1):
                    output.write("- {0}->{1}\n".format(b,r))
                    break
                elif isDistance(b, revc(r), 1):
                    output.write("* {0}->{1}\n".format(b, revc(r)))
                    break
