'''
Created Dec. 26, 2015
@author Carl J. Raymond
'''

# Solve problem using approach in EDTA, but set the cost of a substituion
# to infinite. Allowable options at each step are a match, cost 0, or a gap in S,
# or a gap in T. The cost of a gap is 1.

with open("data/rosalind_scsp.txt") as spec:
    data = spec.read().splitlines()
    
S = data[0]
T = data[1]

len_s = len(S)
len_t = len(T)
print "S (length {0}): {1}".format(len_s, S)
print "T (length {0}): {1}".format(len_t, T)

cost_gap_S = 1
cost_gap_T = 1
#cost_substitute = 1

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

inf = 1000000 # Simulated infinity

# Create each new row, referring to the previous row, and append to the cost matrix
for j in range(len_t):
    thisrow = [ (j+1, 3) ]
    for i in range(len_s):
        prev_cost = lastrow[i][0]
        if S[i] == T[j]:
            # Match.
            thisrow.append( (prev_cost, 0) )
            continue
            
        # Mismatch. Find best action of two possibilities.
        
        # 2. Gap in S
        gap_s = lastrow[i+1][0] + cost_gap_S
        op = (gap_s, 3)
            
        # 3. Gap in T
        gap_t = thisrow[i][0] + cost_gap_T
        if gap_t < op[0]:
            op = (gap_t, 2)
            
        thisrow.append(op)

    cost.append(thisrow)
    lastrow = thisrow

print "Cost matrix:"
for row in cost:
    print row

# The final edit cost is down in the corner
ed = cost[len_t][len_s][0]
print "Edit distance: {0}".format(ed)

# Walk the cost matrix from the far corner back to the origin
# recording the lowest cost alignment sequences in reverse
i, j = len_s, len_t
revalign_s = []
revalign_t = []
revscs = []
while i>0 or j>0:
    step = cost[j][i]
    print step
    action = step[1]
    if action == 0:
        # Match. Consume in S and T.
        i -= 1
        revalign_s.append(S[i])
        j -= 1
        revalign_t.append(T[j])
        revscs.append(S[i])
    elif action == 3:
        # Gap in S, consume in T
        revalign_s.append('-')
        j -= 1
        revalign_t.append(T[j])
        revscs.append(T[j])
    elif action == 2:
        # Gap in T, consume in S
        i -= 1
        revalign_s.append(S[i])
        revalign_t.append('-')
        revscs.append(S[i])

align_s = "".join(revalign_s[::-1])
align_t = "".join(revalign_t[::-1])
result = "".join(revscs[::-1])

print align_s
print align_t
print result

with open("data/rosalind_scsp.out", "w+") as output:
    output.write("{0}\n".format(result))
#    output.write("{0}\n".format(ed))
#    output.write("{0}\n".format(align_s))
#    output.write("{0}\n".format(align_t))
    
