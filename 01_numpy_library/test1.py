import numpy as np

i = np.random.randint(1,50,(3,3))
print(i) 

j = np.random.rand(5,4)
print(j)

np.random.seed(1) #lock randomness to 
print(np.random.randint(1,10,(2,2)))

# ----------------------------------
# random float between 0 and 1
print(np.random.random())

# 1D array of 5 random integers between 0 and 9
print(np.random.randint(0, 10, size=5))

# 2D array (3x3) of random numbers from normal distribution
print(np.random.randn(3, 3))

# Random choice from a list 
print(np.random.choice(['apple', 'banana', 'cherry'], size=2))
