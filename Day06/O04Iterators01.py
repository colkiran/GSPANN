
lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"lst :{lst}")

# print(dir(lst))
iterObj = lst.__iter__()
# print(dir(iterObj))

# __next__ and __iter__ are the protocols of iterable object

elem1 = iterObj.__next__()
print(elem1)

elem2 = next(iterObj)
print(elem2)

elem3 = next(iterObj)
print(elem3)

elem4 = next(iterObj)
print(elem4)

elem5 = next(iterObj)
print(elem5)

elem6 = next(iterObj)
print(elem6)

# elem7 = next(iterObj)
# print(elem7)

print("-" * 60)
for x in lst:
    print(x)
