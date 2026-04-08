import random
import numpy as np
import pandas as pd
# Q1

cubes = list([x ** 3 for x in range(1,11)])
print(cubes)

# Q2

random_samples  = random.sample(range(1,100), 50)
print(np.mean(random_samples))

# Q3
categories  = pd.Series(["apple","banana","orange","grapes","orange","grapes"])
numerical_values = list(map(lambda x: ["apple", "banana", "orange", "grapes"].index(x), categories))
print(numerical_values)

print("---------------")
# Q4
data = [10,20,30,40,50]
mean = np.mean(data)
std = np.std(data)
z_scores = [(x - mean) / std for x in data]
print(z_scores)

# Q5
arr = np.arange(1,10)
arr_transpose = arr.reshape(3,3).T
print(arr)

# Q6
""" SELECT * FROM employee ORDER BY salary DESC LIMIT 3; """


# Q7
# write a program to implement a simple chatbot using if-else statements
def chatbot(user_input):
    if "hello" in user_input:
        return "hello! what's going on?"
    elif "how are you" in user_input:
        print("I'm totally fine,thank you! How about you?")
        user_input = input("you:")
        if ("good" or "fine" or "nice") in user_input:
            return "That's great...." 
    elif "weather" in user_input:
        return "The weather is great today...."
    elif "bye" in user_input:
        return "Goodbye! have a nice day!"
    else:
        return  "sorry, didn't understand that...."
        
while(True):
    user_input = input("you:")
    print("chatbot:",chatbot(user_input))
