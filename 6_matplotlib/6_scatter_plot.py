import matplotlib.pyplot as plt
import numpy  as np
hours = np.array([2,3,4,5,6,7,8,9,10])
marks = np.array([30,35,45,52,60,70,78,83,90])

plt.scatter(hours,marks)
# plt.show()

# --------------------------------------

for h,m in zip(hours,marks):
    plt.text(h,m,f"{m}",fontsize =10)

plt.show() #always below to all that to visualize 