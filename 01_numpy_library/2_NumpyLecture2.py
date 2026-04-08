import numpy as np

a = np.array([[2.5,-25,36.6],[81.2,-64,9]])
b = np.array([[1,2,3],[4,5,6]])
print(a+b)
print("-----------------------------------------")

print("Square Root:\n",np.sqrt(a))
print("Exponential:\n",np.exp(a))

print("-----------------------------------------")


print("Log:\n",np.log([1,np.e,np.e**2]))

print("Power:\n",np.power(a,3))

print("Absolute:",np.abs(a))

print("Round:",np.round(a))

print("Floor:",np.floor(a))
print("ceil:",np.ceil(a))


print("-----------------------------------------")


angle = np.array([0,np.pi/2,np.pi])
print("Sin:",np.sin(angle))
print("Cos:",np.cos(angle))
print("Tan:",np.tan(angle))

 
print("-----------------------------------------")

c = np.array([12,34,56,86,34,83])
print("Minimum:",np.min(c))
print("Maximum:",np.max(c))
print("Mean:",np.mean(c))
print("Median:",np.median(c))
print("Sum:",np.sum(c))
print("Standard Deviation",np.std(c))
print("Variance:",np.var(c))

print("-----------------------------------------")

a = np.array([1,2,3,4,5,6])
reshaped = a.reshape(2,3)
print(reshaped)
print("-----------------------------------------")

transposed = reshaped.T
print(transposed)

print("-----------------------------------------")

reverse_arr = c[::-1]
print(reverse_arr)


print("-----------------------------------------")
flatten_arr = reshaped.flatten() #Does not make changes in the original array
flatten_arr[0] = 100
print(flatten_arr)

print("-----------------------------------------")

# c_copy = c.copy()
# print(c_copy)

# c_view = c.view()
# print(c_view)

# r = reshaped.ravel() #Makes changes in the original array
# print(r)


# Stacking
a = np.array([10,20,30])
b = np.array([11,22,33])

# print("Horizontal Stack:", np.hstack((a,b)))
# print("Vertical Stack:\n", np.vstack((a,b)))

print("Stack Funtion:\n", np.stack((a,b)))
result = np.stack((a,b),axis=1)
print(result)
print("-----------------------------------------")


#Splitting
c = np.array([12,34,53,46,34,75,33,75,86])

print(np.split(c,3))

print("-----------------------------------------")
d = np.array([[1,2,3],[3,4,6]])
print(np.hsplit(d,3))

print("-----------------------------------------")

