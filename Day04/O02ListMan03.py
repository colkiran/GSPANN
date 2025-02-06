
print("count".center(60, "-"))
l1 = [1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")

print(f"l1.count(1) :{l1.count(1)}")
print(f"l1.count(2) :{l1.count(2)}")
print(f"l1.count(3) :{l1.count(3)}")
print(f"l1.count(5) :{l1.count(5)}")

print("index".center(60, "-"))
l1 = [1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")
res = l1.index(3)
print(res)

res = l1.index(3, l1.index(3) + 1)
print(res)

res = l1.index(3, l1.index(3, l1.index(3) + 1) + 1)
print(res)

print(f"copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# to copy the list l1 to l2
l2 = l1         # shallow copy - copy the address with data

print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
# copy
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy the list l3 to l4
l4 = l3.copy()     # deep copy - only the data is copied

print(f"l4 before :{l4}")

l4.extend([11, 12, 13, 14])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
l5 = [1, 2, 3, 4, [2, 4, 6, 8], 5]
print(f"l5 before :{l5}")

# copy the list l5 to l6
l6 = l5.copy()

print(f"l6 before :{l6}")

l6[4].append(10)
l6[4].append(12)
l6[4].append(14)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
l7 = [10, 20, 30, [1, 2, 3, 4, 5], 40, 50]
print(f"l7 :{l7}")

# copy the list l7 to l8
from copy import deepcopy
l8 = deepcopy(l7)

print(f"l8 before :{l8}")

l8[3].extend([6, 7, 8])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

