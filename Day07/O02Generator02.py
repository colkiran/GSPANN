
def my_generator():
    n = 1
    print("apples from  ooty")
    yield n
    n += 9
    print("Oranges from Kanpur")
    yield n
    n += 10
    print("Pine from Cochin")
    yield n

res = my_generator()
print(f"res :{res}")

print(res.__next__())
print(res.__next__())
print(res.__next__())
# print(res.__next__())
