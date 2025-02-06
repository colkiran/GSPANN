"""
sort   - sort will sort the original list
sorted - sorted will return a copy of sorted list
"""


# sort function
l1 = [8, 5, 1, 9, 2, 7, 10, 4, 6, 3]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending order :{res_asc}")

res_des = sorted(l1, reverse=True)
print(f"Descending order :{res_des}")

print("-" * 60)
l1 = [8,'zebra', 5, 'apple', 1, 'x ray', 'blue', 9, 'yellow', 2, 'green', 'white', 7, 'pink', 'violet', 10, 'cat', 'orange', 4, 'hen', 6,'maroon', 3, 'egg', 175, 1234, 29, 259, 2136]
print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(res)

print("-" * 60)
cntr = 0
for i in range(0, len(res)):
    if type(res[i]) == int:
        print(i)
        cntr = i
        break

print(res[:cntr] + sorted(res[cntr:]))

print("-" * 60)
cities = ['thiruvananthapuram', 'bangalore', 'pune', 'chennai', 'delhi', 'vishakapatnam', 'mumbai', 'kolkata', 'mysore', 'ooty']

print(f"cities :{cities}")

print("-" * 60)
# sort this list based on the length of each city name
res_asc = sorted(cities, key=len)
print(f"Ascending order :{res_asc}")

print("reverse".center(60, "-"))
l1 = [1, 2, 3, 4, 5, 6]
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")

