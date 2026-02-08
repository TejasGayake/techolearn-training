import numpy as np

# broadcasting in numpy array
a = np.array([2,3,4,5,6])
print(a+10)

b = np.array([[1,2,3,4,5],[6,7,8,9,10]])  
print(a + b)     #row and column should be matched for both array

print("-------------------------------------------")
# aggregation with  axis

c = np.array([[1,2,3,4,5],[6,7,8,9,10]])   #2d array
print("columnwise: " ,np.sum(c,axis = 0))  # three column ---->give three values

# axis 0 =column wise aggregation
print("rowwise: " ,np.sum(c,axis = 1))   #two rows  ---------> two values

print("-------------------------------------------")

b = np.array([10,20,30,40,50,60,70,80,90,100])
# print(b[( b > 20 ) and ( b < 50)])   #it show error 
print(b[( b > 20 ) & ( b < 50)])   # always use symbol for operator

print("-------------------------------------------")
# sorting
a = np.array([40,20,50,30,60,70,100,90,80])
print("sorted array : ",np.sort(a))


# for 2d array
d = np.array([[30,20,35,87,35,25,64,24],[40,20,50,30,60,70,100,90]])
print("sort array using axis 0 column wise : ",np.sort(d,axis = 0 ))
print("sort array using axis 1 ROW wise : ",np.sort(d,axis = 1  ))

print("-------------------------------------------")

# arg related to indices
print("argsort :")
print(np.argsort(a))   #??
print(np.argmax(a))
print(np.argmin(a))

# np.where
print(np.where(a>65)) # it give indexes of the original values
# >> (array([5, 6, 7, 8]),) ?why like this

print("-------------------------------------------")
# for bifercatio
# np.where(condition ,true_block,false_block)

print(np.where(a>45,"high","low"))
"""interview question (example of categories data bifercation)"""


print("-------------------------------------------")
# search sorted funtion 
# only works on sorted array
sorted_array = np.array([10,20,30,40,50])
print(np.searchsorted(sorted_array,35))  #3
# ?how does it works (searchsorted()) ,and whyy
# -->for percentage values ,example below
# for same range data
# for binary data

print(np.searchsorted(sorted_array,30,side = "left"))
print(np.searchsorted(sorted_array,30,side = "right")) #default right


print("-------------------------------------------")




