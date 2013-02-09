'''
Created on Jan 7, 2013

@author: Carl Raymond
'''

n = 801

r = 1
for i in xrange(n):
    r = r * 2 % 1000000
    
print r
