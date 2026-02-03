import time
import numpy as np

# python  list
lst = list(range(1,1000000)) 
start = time.time()
result = [i*2 for i in lst] #also called list inprehensionn
end = time.time()

print("python list time :-",end-start)

# numpy array 

arr = np.arange(1,1000000) #arange() similar like range() ***
start1 = time.time()
result1 = arr*2          #array broadcasting
end1 = time.time() 
print("Numpy array timee: ",end1-start1)
                    

print(0.4080657958984375-0.013850688934326172)