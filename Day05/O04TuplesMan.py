
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))
print("-" * 60)

t2 = (1, 2, 3.5, 4.6, 'five', 'six', 7+0j, 8-1j, True, False)
print(f"t2 :{t2}")
print(type(t2))
print("-" * 60)

t3 = tuple(range(1, 6))
print(f"t3 :{t3}")
print(type(t3))
print("-" * 60)

t4 = 1, 2, 3, 4, 5
print(f"t4 :{t4}")
print(type(t4))
print("-" * 60)

names = 'jack', 'peter', 'mike'
print(f"names :{names}")
print(type(names))

print("-" * 60)
# print(dir(t1))
t1 = (1, 1, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2)

print(f"t1 :{t1}")

print("count".center(60, "-"))
print(f"count of 1 :{t1.count(1)}")
print(f"count of 2 :{t1.count(2)}")
print(f"count of 3 :{t1.count(3)}")
print(f"count of 6 :{t1.count(6)}")

print("index".center(60, "-"))
print("first occurrence :", t1.index(3))
print("second occurrence :", t1.index(3, t1.index(3) + 1))
print("first occurrence :", t1.index(3, t1.index(3, t1.index(3) + 1) + 1))

