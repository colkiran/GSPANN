
print(sum([x ** 2 for x in range(1, 11)]))      # comprehension
# print([x ** 2 for x in range(1, 11)])
print(sum((x ** 2 for x in  range(1, 11))))     # Generator

from sys import getsizeof
val1 = [x ** 2 for x in range(10000)]
print(f"Comprehension sizeof lst :{getsizeof(val1)}")

# generators will return one element at a time
val2 = (x ** 2 for x in range(10000))
print(f"Generator size of lst :{getsizeof(val2)}")

print("-" * 60)
val3 = (x for x in range(10))
print(val3)

for val in val3:
    print(val)
