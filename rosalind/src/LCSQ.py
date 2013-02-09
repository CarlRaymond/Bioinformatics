'''
Created on Jan 27, 2013

@author: Carl Raymond
'''

def enum(**values):
    return type('Enum', (), values)


with open("rosalind_lcsq.txt") as spec:
    seq1 = spec.readline().strip()
    seq2 = spec.readline().strip()

#seq1 = "AACCTTGG"
#seq2 = "ACACTGTGA"
# A ACCTTG G
# ACAC T GTGA

score_match = 1
score_mismatch = 0
score_skip1 = 0
score_skip2 = 0

Choice = enum(EMPTY=0, SKIP1=1, SKIP2=2, MATCH=3, MISMATCH=4)


print "Seq1 (length {0}):".format(len(seq1))
print seq1
print "Seq2 (length {0}):".format(len(seq2))
print seq2

len1 = len(seq1)
len2 = len(seq2)

matrix = [ [(0, Choice.EMPTY) for j in xrange(len2+1)] for i in xrange(len1+1) ]
for i in xrange(1, len1+1): matrix[i][0] = (0, Choice.SKIP1)
for j in xrange(1, len2+1): matrix[0][j] = (0, Choice.SKIP2)
#for row in matrix: print row


for i in xrange(1, len1+1):
    for j in xrange(1, len2+1):
        if seq1[i-1] == seq2[j-1]:
            best = (matrix[i-1][j-1][0] + score_match, Choice.MATCH)
        else:
            best = (matrix[i-1][j-1][0] + score_mismatch, Choice.MISMATCH)

        skip1 = matrix[i][j-1][0] + score_skip1
        if (skip1 > best[0]):
            best = (skip1, Choice.SKIP1)
        skip2 = matrix[i-1][j][0] + score_skip2
        if (skip2 > best[0]):
            best = (skip2, Choice.SKIP2)
        matrix[i][j] = best

#for row in matrix: print row

# Backtrack

res1 = []
res2 = []

i,j = len1,len2
while i+j > 0:
    c = matrix[i][j][1]
    if c == Choice.MATCH:
        i -= 1
        res1.append(seq1[i])
        j -= 1
        res2.append(seq2[j])
    elif c == Choice.MISMATCH:
        i -= 1
        res1.append(seq1[i])
        res1.append(" ")
        j -= 1
        res2.append(" ")
        res2.append(seq2[j])
    elif c == Choice.SKIP1:
        res1.append(" ")
        j -= 1
        res2.append(seq2[j])
    elif c == Choice.SKIP2:
        i -= 1
        res1.append(seq1[i])
        res2.append(" ")
    else:
        pass

#print res1
#print res2

longest = list([a for (a,b) in zip(res1, res2) if a == b])
longest.reverse()
print "Longest subsequence (length {0}): ".format(len(longest))
final = "".join(longest)
print final

with open("rosalind_lcsq.out.txt", "w+") as output:
    output.write(final)

