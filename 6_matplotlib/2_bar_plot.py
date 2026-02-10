# for showin segments bar plot
import matplotlib.pyplot as plt

product = ["Laptop","Mobile","Tablet","Headphones"]
sales = [80,150,80,90]

# ---------------------------------------
""" normal horizontal graph"""


# plt.figure(figsize=(6,4))
# plt.bar(product,sales)
# plt.xlabel("Product Names")
# plt.ylabel("Sales Per Month")
# plt.title("2025 Sales graph")
# # due to y axis it is vertical
# # axis = x for horizontal
# plt.grid(axis = "y",linestyle = '--',alpha = 0.5) #alpha -->opacity
# plt.show()


# ---------------------------------------
""" horizontal bar chart """

# # please mind axis names while horizontal

# plt.barh(product,sales)
# plt.xlabel("Sales Per Month")
# plt.ylabel("Product Names")
# plt.title("horizontal bar chart")
# # axis = x for horizontal
# plt.grid(axis = "x",linestyle = '--',alpha = 0.4) #alpha -->opacity
# plt.show()

# ---------------------------------------

sales_24 = [80,150,60,90]
sales_25 = [90,150,65,70]
# product written earlier

plt.title("Sales comparison graph")
plt.plot(product,sales_25,label = "2025 Sales Data",color = "red",linestyle = '-',marker = "*")
plt.plot(product,sales_24,label = "2024 Sales Data",color = "green",linestyle = '-.',marker = 'o')

plt.legend()
plt.show()
# ---------------------------------------

