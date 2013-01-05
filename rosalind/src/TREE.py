'''
Created on Jan 3, 2013

@author: Carl Raymond
'''

with open("rosalind_tree.txt") as spec:
    n = int(spec.readline().strip())
    edges = [  tuple([int(x) for x in line.split(' ')]) for line in spec ]
    
print "{0} nodes".format(n)
print "{0} edges".format(len(edges))

# Create fully disconnected graph of size n. Element 0 is unused
roots = range(n+1)
roots[0] = -1

# Form the connected components.  Nodes in the same
# component have the same root node, which is the
# node of the smallest id
for (u,v) in edges:
    ru,rv = roots[u],roots[v]
    if ru < rv:
        roots[v] = ru
    else:
        roots[u] = rv
print roots[1:]
for (i, r) in enumerate(roots):
    while r != roots[r]: r = roots[r]
    roots[i] = r
print roots[1:]
    
# Count connected component roots -- nodes whose root is itself
distinctRoots = [ i for (i, r) in enumerate(roots) if i == r]
print "{0} distinct roots: ".format(len(distinctRoots)), distinctRoots

components = [ [i for i,r in enumerate(roots) if r==root and i>0] for root in distinctRoots ]
print "Connected components:"
for c in components: print c
