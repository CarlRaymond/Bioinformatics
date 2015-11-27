'''
Created on Nov. 24 2015
@author: Carl J. Raymond
'''

# Solves both EDIT and EDTA.

from fasta import read


with open("rosalind_edta.txt") as spec:
    data_s, data_t = read(spec)

_, S = data_s
len_s = len(S)
_, T = data_t    
len_t = len(T)
print "S (length {0}): {1}".format(len_s, S)
print "T (length {0}): {1}".format(len_t, T)

cost_gap_S = 1
cost_gap_T = 1
cost_substitute = 2

# Allocate and initialize the cost array. Each cell is a tuple consiting of a
# cost and an operation token that describes how we got to this place from
# the previous step. The token 0 means that the characters matched; 1 means they
# didn't match, and the choice is to substitute; 2 means that a position
# in S was skipped; 3 means a postion in T was skipped.
# Cost[0][j] = (j,3) for all j and cost[i][0] = (i,2) for all i. This
# represents the cost of a gap from positions 1..i of S or T.

# Create first row of cost matrix
lastrow = [ (i, 0 if i==0 else 2) for i in range(len_s+1)]
cost = [ lastrow ]

# Create each new row, referring to the previous row, and append to the cost matrix
for j in range(len_t):
    thisrow = [ (j+1, 3) ]
    for i in range(len_s):
        prev_cost = lastrow[i][0]
        if S[i] == T[j]:
            # Match.
            thisrow.append( (prev_cost, 0) )
            continue
            
        # Mismatch. Find best action of three possibilities.
        # 1. Substitute
        substitute = prev_cost + cost_substitute
        op = (substitute, 1)
        
        # 2. Gap in S
        gap_s = thisrow[i][0] + cost_gap_S
        if gap_s < op[0]:
            op = (gap_s, 2)
            
        # 3. Gap in T
        gap_t = lastrow[i+1][0] + cost_gap_T
        if gap_t < op[0]:
            op = (gap_t, 3)
            
        thisrow.append(op)

    cost.append(thisrow)
    lastrow = thisrow

#for row in cost:            
#    print row

# The final edit cost is down in the corner
ed = cost[len_t][len_s][0]
print "Edit distance: {0}".format(ed)

# Walk the cost matrix from the far corner back to the origin
# recording the lowest cost alignment sequences in reverse
i, j = len_s, len_t
revalign_s = []
revalign_t = []
while i>0 or j>0:
    step = cost[j][i]
    #print step
    action = step[1]
    if action == 0 or action == 1:
        # Match or mismatch. Consume in S and T.
        i -= 1
        revalign_s.append(S[i])
        j -= 1
        revalign_t.append(T[j])
    elif action == 2:
        # Gap in T, consume in S
        i -= 1
        revalign_s.append(S[i])
        revalign_t.append('-')
    elif action == 3:
        # Gap in S, consume in T
        revalign_s.append('-')
        j -= 1
        revalign_t.append(T[j])

align_s = "".join(revalign_s[::-1])
align_t = "".join(revalign_t[::-1])

with open("rosalind_edta.out", "w+") as output:
    output.write("{0}\n".format(ed))
    output.write("{0}\n".format(align_s))
    output.write("{0}\n".format(align_t))
    
