'''
Created on Dec 10, 2012

@author: Carl Raymond
'''

import urllib
import re
import fasta

"""Finds (overlapping) occurrences of pattern N{P}[ST]{P} in a sequence"""

# Matches can overlap, so use a positive lookahead assertion (tricky!)
pattern = "(?=(N[^P][ST][^P]))"

with open("rosalind_mprt.txt") as seqlist:
    for name in seqlist:
        name = name.strip()
        data = urllib.urlopen("http://www.uniprot.org/uniprot/" + name + ".fasta")
        for desc, data in fasta.read(data):
            if re.search(pattern, data):
                print name
                positions = [match.start() for match in re.finditer(pattern, data)]
                for pos in positions:
                    print pos+1,
                print