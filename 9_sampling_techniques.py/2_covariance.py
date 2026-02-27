# =================================================
#  Covariance **
# =================================================
print('='*70)

import numpy as np
x = np.array([10,20,30,40,50,60])
y = np.array([60,50,40,30,20,10])

# covariance from scratch ======================================
mean_x = x.mean()
mean_y = y.mean()

print("Mean of X: ",mean_x)
print("Mean of Y: ",mean_y)

covariance = (((x-mean_x)*(y-mean_y)).sum())/ (len(x)-1)
print("Covariance: ",covariance)

print('='*70)

# using covariance function====================================
cov = np.cov(x,y)
print("whole matrix of covariance:\n",cov)
"""
[[ cov(x) , cov(x,y)]
 [ cov(y,x),cov(y)]]
"""
print("Covariance" ,cov[0][1])

print('='*70)


