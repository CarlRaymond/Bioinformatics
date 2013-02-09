'''
Created on Jan 4, 2013

@author: Carl Raymond
'''

from itertools import count
from sys import exit

def enum(**values):
    return type('Enum', (), values)

Tokens = enum(LPAREN=1, RPAREN=2, COMMA=3, SEMI=4, NAME=5)

def nameGenerator(prefix):
    for n in count(1):
        yield prefix + str(n)
        
def tokenize(treespec):
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

def emitNode(stream, node):
    stream.write ("node {0} [ label=\"{1}\"];\n".format(node, node.replace("_", "\\n")))
    
def emitEdges(stream, parent, children):
    for c in children:
        stream.write("{0} -- {1}\n".format(parent, c))

with open("rosalind_nwck.txt") as spec:
    treespec = spec.readline().strip()
    targetnodes = [ name for name in spec.readline().strip().split()]
    
print treespec
print targetnodes


with open("NWCK.gv", "w+") as graph:
    graph.write("graph G { graph [overlap=false, splines=false]; \n")
    
    stack = []
    children = []
    name = None
    assignedNames = nameGenerator("V")
    prevToken = None
    for token in tokenize(treespec):
        ttype = token[0]
        if ttype == Tokens.LPAREN:
            stack.append(children)
            children = []
        elif ttype == Tokens.COMMA:
            pass
        elif ttype == Tokens.RPAREN:
            lastchildren = children
            children = stack.pop()
        elif ttype == Tokens.NAME:
            name = token[1] or assignedNames.next()
            emitNode(graph, name)
            if prevToken and prevToken[0] == Tokens.RPAREN:
                emitEdges(graph, name, lastchildren)
                
            children.append(name)
        elif ttype == Tokens.SEMI:
            pass
            
        prevToken = token
    graph.write("}\n")