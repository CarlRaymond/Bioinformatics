'''
Created Nov. 29, 2015
@author Carl J. Raymond
'''

s = 'AUAUGCGC'

c = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 
    'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

def motz(s):
    if s not in c:
        c[s] = motz(s[:-1]) + sum([motz(s[1:k]) * c[s[0]+s[k]] * motz(s[k+1:]) for k in range(1, len(s))])
    return c[s]
	
print s
print motz(s)
