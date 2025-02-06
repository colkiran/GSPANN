

# print("-" * 60)
# print(dir(l1))

print("append".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])

print(f"l1 :{l1}")

print("extend".center(60, "-"))
l2 = list(range(1, 6))
print(f"l2 :{l2}")

l2.extend([6, 7, 8])
l2.extend([9, 10])

print(f"l2 :{l2}")
l2.extend([11])

print("insert".center(60, "-"))
l3 = list(range(1, 6))
print(f"l3 :{l3}")

l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)

print(f"l3 :{l3}")
print(f"len(l3) :{len(l3)}")

l3.insert(15, 10)
print(f"len(l3) :{len(l3)}")

# delete values
print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")
# will return the values that were removed from the list

ret = l1.pop(7)
print(f"ret :{ret}")

ret = l1.pop(3)
print(f"ret :{ret}")

ret = l1.pop()
print(f"ret :{ret}")

ret = l1.pop()
print(f"ret :{ret}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))
l2 = [1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1]

print(f"l2 :{l2}")
l2.remove(3)
l2.remove(3)
l2.remove(3)

print(f"l2 :{l2}")

l1 = [1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2,]

# while 2 in l1:
#     l1.remove(2)
# print(l1)

print([i for i in l1 if i != 2])

print("clear".center(60, "-"))
l1 = list(range(10, 101, 10))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")
