import matplotlib.pyplot as plt

# mostly use for 3 to 6 categories

brands = ["Brand A","Brand B","Brand C","Brand D"]
share = [40,20,20,20]
# ---------------------------------------
# *** autopct = ?  

color = ["red","purple","lightpink","blue"]
plt.pie(share,labels = brands,autopct = "%1.1f%%",colors = color,startangle = 90) #till autopct mandatory
plt.title("Market Share of Brands")
plt.show()

# ---------------------------------------
# subplot = adding two or multiple plot in single plot