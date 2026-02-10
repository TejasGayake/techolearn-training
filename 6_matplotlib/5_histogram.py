import matplotlib.pyplot as plt
import numpy as np


ages = [22,27,30,25,26,27,50,37,45,26,34,24,25,64,65,23,54,10,12,5,24,12,42,1,2,5,12,10,9,8]
plt.hist(ages,bins = 5,density = True,alpha = 0.5,edgecolor = "Black")
# bins =>for five bars

# plt.show()


# for adding line plot in it

count, bin_edges = np.histogram(ages,bins = 5,density =True)
# center point in bar --->bin_center is used
bin_centers = ((bin_edges[:-1] + bin_edges[1:])/2)
plt.plot(bin_centers,count,marker = "+",linestyle= "-.",color = "red")
plt.show()