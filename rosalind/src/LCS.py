'''
Created on Dec 15, 2012

@author: carl
'''

from suffix_tree import GeneralisedSuffixTree

def validateSubstring(strings, seq):
    for s in strings:
        if s.find(seq) == -1:
            return False
    return True

    
with open('rosalind_lcs.txt') as spec:
    data = [seq.strip() for seq in spec]
    
    # The generalized suffix tree doesn't work well with a large number of strings.
    # Use the first 10 to generate candidates, and then compare each candidate
    # (in decreasing length order) to the data to find a common substring.
    tree = GeneralisedSuffixTree(data[:10])
    candidates = []
    for shared in tree.sharedSubstrings(5):
        for seq, start, stop in shared:
            candidates.append(tree.sequences[seq][start:stop])
            break
    
    candidates.sort(cmp=None, key=lambda s: len(s), reverse=True)
    for c in candidates:
        if validateSubstring(data, c):
            print c
            print len(c)
            break
    else:
        print "No common string found!"
        