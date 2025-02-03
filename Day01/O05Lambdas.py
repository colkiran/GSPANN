
def add(x, y):
    return x + y

# print(add(20, 40))
a = add

res = a(100, 200)
print(f"res :{res}")

print("-" * 60)
b = lambda x, y : x + y
res = b(45, 66)
print(f"res :{res}")

print("-" * 60)
# lambdas are best used with  1. map, 2, filter, 3.reduce

print("Map".center(60, "-"))
lst = list(range(1, 11))
print(f"lst :{lst}")

squares = list(map(lambda x : x ** 2, lst))
print(f"squares :{squares}")