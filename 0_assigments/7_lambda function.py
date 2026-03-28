from functools import reduce
# 1
num1 = [1,2,3,4,5]
cubes = list(map(lambda x : x**3,num1))
print(cubes)

# 2
num2 =  [2,3,4,5,6,7,8,9,10]
prime = list(filter(lambda x : all(x % i != 0 for i in range(2, int(x**0.5)+1)), num2))
print(prime)

# 3
num3 = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, num3)
print(product) 

# 4
result = lambda marks : "Pass" if marks >=40 else "Fail"
print("Result :",result(70))

# 5
discount = lambda price : price - (price * 0.15)
print("discounted price: ",discount(300))

# 6
tsalary = lambda basic : basic + (basic*0.1)
print(tsalary(30000))

# 7
gst = lambda price : price + (price*0.18)
print(gst(50000))

# 8. 
clean_username = lambda s: s.strip().lower()
print(clean_username(" SANTOSHI "))


# 9.
reverse = lambda s: s[::-1]
print(reverse("Python"))


# 10.
area = lambda r: 3.14 * r * r
print(area(5))


# 11.
check = lambda n: n % 3 == 0 and n % 5 == 0
print(check(15))




