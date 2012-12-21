'''
Created on Dec 17, 2012

@author: Carl Raymond
'''

n1 = 19918
n2 = 16652
n3 = 18782
n4 = 19395
n5 = 18188
n6 = 17767

s = n1+n2+n3+n4+n5+n6

p = 0
p += n1 * 2.0           # AA-AA
p += n2 * 2.0           # AA-Aa
p += n3 * 2.0           # AA-aa
p += n4 * 1.5           # Aa-Aa
p += n5 * 1.0           # Aa-aa
p += n6 * 0             # aa-aa

print p
