'''
Created on Nov. 24 2015
@author: Carl J. Raymond
'''

# Solves both EDIT and EDTA.

from fasta import read


with open("rosalind_edta.txt") as spec:
    data_s, data_t = read(spec)

name_s, seq_s = data_s
len_s = len(seq_s)
name_t, seq_t = data_t    
len_t = len(seq_t)
print "S ({0}) length {1}: {2}".format(name_s, len_s, seq_s)
print "T ({0}) length {1}: {2}".format(name_t, len_t, seq_t)

cost_gap_s = 1
cost_gap_t = 1
cost_mismatch = 1

# Allocate and initialize the cost array. Each cell is a tuple consiting of a
# cost and an operation token that describes how we got to this place from
# the previous step. The token 0 means that the characters matched; 1 means they
# didn't match, and the choice is to allow a mismatch; 2 means that a position
# in S was skipped; 3 means a postion in T was skipped.
# Cost[0][j] = (j,3) for all j and cost[i][0] = (i,2) for all i. This
# represents the cost of a gap from positions 1..i of S or T.

# Create first row of cost matrix
lastrow = [ (i, 0 if i==0 else 2) for i in range(len_s+1)]
cost = [ lastrow ]

for j in range(len_t):
    thisrow = [ (j+1, 3) ]
    for i in range(len_s):
        prev_cost = lastrow[i][0]
        if seq_s[i] == seq_t[j]:
            # Match.
            thisrow.append( (prev_cost, 0) )
            continue
            
        # Mismatch. Find best action of three possibilities.
        # 1. Let mismatch stand
        mismatch_cost = prev_cost + cost_mismatch
        op = (mismatch_cost, 1)
        
        # 2. Gap in S
        skip_s_cost = thisrow[i][0] + cost_gap_s
        if skip_s_cost < op[0]:
            op = (skip_s_cost, 2)
            
        # 3. Gap in T
        skip_t_cost = lastrow[i+1][0] + cost_gap_t
        if skip_t_cost < op[0]:
            op = (skip_t_cost, 3)
            
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
        revalign_s.append(seq_s[i])
        j -= 1
        revalign_t.append(seq_t[j])
    elif action == 2:
        # Gap in T, consume in S
        i -= 1
        revalign_s.append(seq_s[i])
        revalign_t.append('-')
    elif action == 3:
        # Gap in S, consume in T
        revalign_s.append('-')
        j -= 1
        revalign_t.append(seq_t[j])

align_s = "".join(revalign_s[::-1])
align_t = "".join(revalign_t[::-1])

with open("rosalind_edta.out", "w+") as output:
    output.write("{0}\n".format(ed))
    output.write("{0}\n".format(align_s))
    output.write("{0}\n".format(align_t))
    
