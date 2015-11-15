'''
Created on Feb 10, 2013

@author: Carl Raymond
'''

with open("rosalind_lgis.txt") as spec:
    n = int(spec.readline())
    perm = [0] + [int(k) for k in spec.readline().split()]

#n = 9
#perm = [0] + [12, 1, 2, 13, 3, 14, 15, 4, 16, 17, 18, 19, 20, 5, 6, 7, 8, 9, 11, 10]
#perm = [0] + [1, 2, 3, 4, 5, 6, 7, 8, 9]
#perm = [0] + [9, 8, 7, 6, 5, 4, 3, 2, 1]  
#perm = [0] + [4, 3, 5, 1, 8, 2, 7, 6, 9]
#perm = [0] + [3, 4, 5, 6, 7, 8, 9, 1, 2]
#perm = [0] + [1,2,3,7,8,9,4,5,6]
#perm = [0] + [6, 7, 8, 4, 5, 1, 2, 3, 9]

#formatted = ", ".join(["{0:2}".format(e) for e in perm[1:]])
#print "{0:2}: ".format(n), formatted


# The pathinc (pathdec) array holds pairs (len, pos) where len is the length of
# the longest increasing (decreasing) subsequence ending at that point, and pos is
# the index of the preceding element of the subsequence of that length. 
pathinc = [(0,0)] * (n+1)
pathinc[0] = (0, None)
pathdec = [(0,0)] * (n+1)
pathdec[0] = (0, None)

# Build pathinc
for i in xrange(1, n+1):
    bestinc = (0, 0)
    for j in xrange(i):
        if (perm[i] > perm[j] and pathinc[j][0] >= bestinc[0]):
            bestinc = (pathinc[j][0]+1, j)
    pathinc[i] = bestinc

maxposinc = 0
for i in xrange(n+1):
    if pathinc[i][0] > pathinc[maxposinc][0]:
        maxposinc = i

# Form the longest increasing subsequence by working backward
increasing = [perm[maxposinc]]
nextpos = pathinc[maxposinc][1]
while nextpos:
    increasing.append(perm[nextpos])
    nextpos = pathinc[nextpos][1]
increasing.reverse()
#print "Increasing:"
for x in increasing: print x,
print

# Build pathdec
perm[0] = n+1
for i in xrange(1, n+1):
    bestdec = (0, 0)
    for j in xrange(i):
        if (perm[i] < perm[j] and pathdec[j][0] >= bestdec[0]):
            bestdec = (pathdec[j][0]+1, j)
    pathdec[i] = bestdec
    

# Find maximum length and position of increasing and decresing sequences
maxposdec = 0
for i in xrange(n+1):
    if pathdec[i][0] > pathdec[maxposdec][0]:
        maxposdec = i


decreasing = [perm[maxposdec]]
nextpos = pathdec[maxposdec][1]
while nextpos:
    decreasing.append(perm[nextpos])
    nextpos = pathdec[nextpos][1]
decreasing.reverse()
#print "Decreasing:"
for x in decreasing: print x,
print

