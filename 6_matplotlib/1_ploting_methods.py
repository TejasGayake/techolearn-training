import matplotlib.pyplot as plt
import numpy as np

# all things can be called ,series ,list ,numpy array or dataframe
hours = np.array([2,3,4,5,6,7,8,9,10])
marks = np.array([30,35,40,42,50,57,60,66,70])
"""
plt.plot(hours,marks)
plt.xlabel("hours of study")
plt.ylabel("Marks")
plt.title("Hours study vs Marks (linegraph)")
plt.show()
"""
# ================================================
# after adding marker

"""
# marker can be anything
# ?some shortcuts for symbols
# s for square
# many more for symbols

plt.plot(hours,marks,marker="d")
plt.xlabel("hours of study")
plt.ylabel("Marks")
plt.title("Hours study vs Marks (linegraph)")
plt.show()
"""
# ================================================

# after changing line style


# using (linestyle = "") *inside the plot function

plt.plot(hours,marks,marker="d",linestyle = "-.")
plt.xlabel("hours of study")
plt.ylabel("Marks")
plt.title("Hours study vs Marks (linegraph)")
plt.show()

# ================================================

# after changing colour of line and marker

"""
# color = "green",
# markerfacecolor="red",
# markersize=15,
# markeredgewidth= 5

plt.plot(hours,marks,marker="d",linestyle = "-.",color = "green",markerfacecolor="red",markersize=15,markeredgewidth= 3)
plt.xlabel("hours of study")
plt.ylabel("Marks")
plt.title("Hours study vs Marks (linegraph)")
plt.show()
"""
# ================================================
# resize of plot

"""
# >>figure(figsize = (5,7)) --->plot window
 
plt.figure(figsize = (5,7))
plt.plot(hours,marks,marker="d",linestyle = "-.",color = "green",markerfacecolor="red",markersize=15,markeredgewidth= 3)
plt.xlabel("hours of study")
plt.ylabel("Marks")
plt.title("Hours study vs Marks (linegraph)")
plt.show()
"""
# ================================================
# grid line horizontal or vertical or both

# plt.figure(figsize = (5,7))
# plt.plot(hours,marks,marker="d",linestyle = "-.",color = "green",markerfacecolor="red",markersize=15,markeredgewidth= 3)
# plt.xlabel("hours of study")
# plt.ylabel("Marks")
# plt.title("Hours study vs Marks (linegraph)")
# plt.grid(linestyle = "--",alpha = 0.5)
# plt.show()
