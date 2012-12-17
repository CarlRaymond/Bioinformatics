'''
Created on Dec 17, 2012

@author: Carl Raymond
'''

k = float(22)
m = float(21)
n = float(17)


s = k+m+n

p = 0

p += k/s * (k-1)/(s-1)          # KK 
p += k/s * m/(s-1)              # KM
p += k/s * n/(s-1)              # KN
p += m/s * k/(s-1)              # MK
p += m/s * (m-1)/(s-1) * .75    # MM
p += m/s * n/(s-1) * 0.5        # MN
p += n/s * k/(s-1)              # NK
p += n/s * m/(s-1) * 0.5        # NM
p += n/s * (n-1)/(s-1) * 0      # NN

print p