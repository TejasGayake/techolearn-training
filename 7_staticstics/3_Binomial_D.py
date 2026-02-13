from math import comb,factorial,exp,sqrt,pi
import matplotlib.pyplot as plt
import statistics
import numpy as np

from scipy.stats import binom


# if coins are shuffled or tossed
n = 4                  # -coin tossed 4 times
k = 2 #successes
p = 0.5 #probability

# for finding combination

prob = comb(n,k)*(p**k)*((1-p)**(n-k))

print(f"Probability of Exactly {k} Success in {n} trails is :- {prob} --->binomial distribution")
# ---------------------------------
# ploting this 
# using bar plot



# plt.bar(k,prob)
# plt.title("binomial distribution")
# plt.xlabel("k")
# plt.ylabel("Probability")
# plt.show()


print('-------------------------------')

n = 10
p = 0.5

k_binom = np.arange(0,n+1)  #arange(0,n-1)
binom_prob = binom.pmf(k_binom,n,p)

print("Binomial Probality : ",binom_prob)
print("Mean : ",binom.mean(n,p))
print("Variance : ",binom.var(n,p))

plt.figure()
plt.bar(k_binom,binom_prob)
plt.title("Binomial Distribution")
plt.ylabel("Probability")
plt.show()