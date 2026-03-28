# --------------------------------------
# 1
def num_gen(n):
    for i in range(1,n+1):
        yield i
for i in num_gen(30):
    print(i)
# --------------------------------------
# 2
def even_gen():
    for i in range(2,21,2):
        yield i
for i in even_gen():
    print(i)

# --------------------------------------
# 3
def fibb_gen(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b
for i in fibb_gen(10):
    print(i)

# --------------------------------------
# 4
squares = (x**2 for x in range(1,11))
for sq in squares :
    print(sq)

# --------------------------------------
# 5
def char_gen(string):
    for i in string:
        yield i
for i in char_gen("Tejas"):
    print(i)   


