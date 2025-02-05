
l1 = list()
print(f"l1 :{l1}")
print(type(l1))
print("-" * 60)

l2 = [1, 2, 3, 4, 5.1, 6.9, 7,5, 8.0, 9 + 2j, 10-3j, 'eleven', 'twelve', 'thirteen', 'True', 'False']
print(f"l2 :{l2}")
print(type(l2))
print("-" * 60)

l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))
print("-" * 60)

print("-" * 60)
# CRUD
# create
l1 = list(range(1, 6))
print(f"l1 :{l1}")

print("-" * 60)
# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")
print(f"l1[-1] :{l1[-1]}")

for i in l1:
    print(i, end=" ")
print()

print("-" * 60)
# update - insert, modify
print(f"l1 :{l1}")
# modify
l1[2] = 300
print(f"l1 :{l1}")

# insert - not possible
l1[3] = 450
print(f"l1 :{l1}")

print("-" * 60)
# delete
print(f"l1 :{l1}")
del[l1[2]]
del[l1[-1]]

print(f"l1 :{l1}")
