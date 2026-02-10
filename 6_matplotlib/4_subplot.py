# subplot = adding two or multiple plot in single plot
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2)

# left subplot
x = np.array([2,3,4,5,6,7,8,9,10])
y = np.array([30,35,40,42,50,57,60,66,70])

axes[0].plot(x,y,marker = "*")
axes[0].set_title("Line Chart")
axes[0].set_xlabel("X Axis Value")
axes[0].set_ylabel("Y Axis Value")
axes[0].grid(True)

# bar chart
product = ["Laptop","Mobile","Tablet","Headphones"]
sales = [80,150,80,90]

axes[1].bar(product,sales)
axes[1].set_title("Product wise Sales Bar Graph")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Sales")

plt.show()


