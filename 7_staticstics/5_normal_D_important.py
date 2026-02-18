"""
z score
"""

import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#  \?? purpose of using normal distribution 

data  = [10,12,14,16,18]
data  = [24,23,63,64,23,64,23,78,95,47]

mean = statistics.mean(data)

std = statistics.stdev(data)

value = 70

z = (value-mean)/std

print("data : ",data)
print("Mean :",mean)
print("Standard Deviation : ",std)
print("Value :",value)
print("z-score :",z)

if z >= 0 and z<=1:
    print("Probability is between 50% to 85%")
elif z >1 and z<=2:
    print("probability is between 86% and 95%")
else: 
    print("Probability interpretation is depends on z Range")

# ================================================
# normal distribution

y = (1/(std*np.sqrt(2*np.pi))) * np.exp(-0.5*(z**2))

print("Normal Distribution : ",y)

# ==============================================
# using scipy.stats

mean = 100
std_dev  = 15
# when std muliple of 4 then probability goes to zero

x = np.linspace(mean - 4*std_dev,mean + 4*std_dev,200)
# pdf ---->probability density function
normal_pdf = norm.pdf(x,mean,std_dev)
print("Normal Distribution ",normal_pdf)

# Bell-shape curve

plt.figure()
plt.plot(x,normal_pdf)
plt.axvline(mean,linestyle= "--")
plt.title("Normal Distribution")
plt.xlabel("X")
plt.ylabel("Probability")

plt.show()
