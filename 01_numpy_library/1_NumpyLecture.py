import numpy as np

a = np.array([34,45,67,45,75,34,23])
print(a)
print(type(a))

print("--------------------------------")

b = np.array([[12,45,64],[75,34,87]])
print("2D Array:-\n",b)
print(type(b))

print("--------------------------------")

c = np.zeros((4,4))
print(c)

print("--------------------------------")

c = np.zeros((4,4))
print("matrix with zeros :\n",c)

print("--------------------------------")

d = np.ones((4,3),dtype = int)
d1 = np.ones((4,3)) #by default float
print("Matrix with ones\n",d1)
print("Matrix with ones\n",d)

print("--------------------------------")

e = np.full((3,3),6)
print("Matrix with full of 6 :\n",e)

print("--------------------------------")

#identity matrix
f = np.eye(3,5 , k = 1)  #index of diagonal
                         #upper d.. (k>0),lower d..(k<0)
print(f)

print("--------------------------------")
# funtion is similar to range

g = np.arange(1,11,2) # arange(start,stop-1,step)
print(g)              # arange(start, n-1  ,condition <not works>)

print("--------------------------------")

h = np.linspace(1,10,4) #generate 4 numbers with equi distance including 1 & 10
print(h)

print("--------------------------------")

# i = np.random.randint(1,50,(3,3))
# print(i) 

# j = np.random.rand(5,4)
# print(j)

# np.random.seed(1) #lock randomness to 
# print(np.random.randint(1,10,(2,2)))

# ----------------------------------
# random float between 0 and 1
print(np.random.random())

# 1D array of 5 random integers between 0 and 9
print(np.random.randint(0, 10, size=5))

# 2D array (3x3) of random numbers from normal distribution
print(np.random.randn(3, 3))

# Random choice from a list
print(np.random.choice(['apple', 'banana', 'cherry'], size=2))

# ----------------------------------

# Array Attributes

# arr = np.array([[1,2,3],[7,4,3],[8,5,8]])
# print(arr)
# print("Shape:-",arr.shape)
# print("Dimension:-",arr.ndim)
# print("Size:-",arr.size)
# print("DataType:-",arr.dtype)
# print("ItemSize:-",arr.itemsize)
# print("TotalSize:-",arr.nbytes)

# a = np.array([34,45,67,45,75,34,23])
# print(a[-1])



arr = np.array([[1,2,3],[7,4,0]])

print(arr[0][1])
print(arr[1,2])



print(np.random.random(15))