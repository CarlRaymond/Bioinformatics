'''
Created on Jan 4, 2013

@author: Carl Raymond
'''

def enum(**values):
    return type('Enum', (), values)

Tokens = enum(LPAREN=1, RPAREN=2, COMMA=3, SEMI=4, NAME=5)

def tokenize(treespec):
    pos = 0
    n = len(treespec)
    name = []
    for c in treespec:
        if c == '(':
            yield (Tokens.LPAREN,)
        elif c == ')':
            yield (Tokens.NAME, "".join(name))
            name = []
            yield (Tokens.RPAREN,)
        elif c == ',':
            yield (Tokens.NAME, "".join(name))
            name = []
            yield (Tokens.COMMA,)
        elif c == ';':
            yield (Tokens.NAME, "".join(name))
            name = []
            yield (Tokens.SEMI,)
        else:
            name.append(c)


with open("rosalind_nwck.txt") as spec:
    treespec = spec.readline().strip()
    targetnodes = [ name for name in spec.readline().strip().split()]
    
print treespec
print targetnodes

for token in tokenize(treespec):
    print token
