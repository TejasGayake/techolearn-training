from math import comb,factorial,exp,sqrt,pi
import matplotlib.pyplot as plt
import statistics
import numpy as np

from scipy.stats import poisson

lamb = 3
k = 2

# e^x == exp(x)
prob = (exp(-lamb)*(lamb**k))/factorial(k)

print("Poisson Distribution : ",prob)

# plotting poisson 


# plt.bar(k,prob)
# plt.title("Possion Distribution")
# plt.xlabel("No. of events")
# plt.ylabel("Probability")
# plt.show()



# ===============================================
" Discret variable probability function "
# ploting using sci.py library
# pmf() --->probability mass function
# binom.pmf()--->binomial distribution
# poisson.pmf() -->poisson distribution



lamb = 4
k_poisson = np.arange(0,15)
poisson_prob = poisson.pmf(k_poisson,lamb)
print("Possion Distribution : ",poisson_prob)

plt.figure()
plt.bar(k_poisson,poisson_prob)
plt.title("Poisson Distribution")
plt.xlabel("No. of events k")
plt.ylabel("Probality")
plt.show()