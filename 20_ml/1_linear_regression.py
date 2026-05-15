import pandas as pd 
from sklearn.linear_model import LinearRegression

data = {
    "Study_Hours":[1,2,3,4,5],
    "Marks":[50,55,60,65,70,]
}

df = pd.DataFrame(data)
print(df)

x = df[["Study_Hours"]]
y = df[["Marks"]]

model = LinearRegression()
model.fit(x,y)

print("Intercept;-",model.intercept_)
print("Slope(m):-",model.coef_)


print("\n Regression Equation")
print("Y = mX+C ", model.coef_* (7) + model.intercept_ )

hours = float(input("Enter Study Hours:-"))
new_hour = pd.DataFrame({"Study_Hours":[hours]})
predicted_marks = model.predict(new_hour)
print("Predicted Marks for 8 hours of study:- ",predicted_marks)
