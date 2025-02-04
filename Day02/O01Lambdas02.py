
# map
print("filter".center(60, "-"))
l1 = list(range(1, 31))
print(f"l1 :{l1}")

print("-" * 60)
# lambda expression should return a true or a false
mul_three = list(filter(lambda x : x % 3 == 0, l1))
print(f"multiples of three :{mul_three}")

sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

words = list(filter(lambda x : x != 'the', sentence.split()))
print(f"words :{words}")

print("-" * 60)
words = list(filter(lambda x : len(x) == 3, sentence.split()))
print(f"words :{words}")

print("-" * 60)
sentence = "the quick brown stress fox  prompt jumps over the lazy dog"
words = list(filter(lambda x : x.replace('t', '') if 't' in x else x, sentence.split()))
print(f"words :{words}")

print("-" * 60)
# reduce = functools
from functools import reduce

l1 = [6, 4, 1, 8, 3, 5, 7]
print(f"l1 :{l1}")

res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

l2 = list(range(1, 11))
print(f"l2 :{l2}")
res = reduce(lambda x, y: x + y, l2)
print(f"res :{res}")
