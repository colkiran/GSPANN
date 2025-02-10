
values = list(range(10, 40, 10))
print(f"values :{values}")

# upack the value from the list
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values
print(a, b, c, sep=", ")
print("-" * 60)

a, *b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

*a, b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(len(lst3))
print(f"lst3 :{lst3}")
print("-" * 60)

lst4 = [*lst1, *lst2]               # unpack
print(len(lst4))
print(f"lst4 :{lst4}")
print("-" * 60)

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"letters :{letters}")
print("-" * 60)

for letter in letters:
    print(letter, end=" ")
print()
print("-" * 60)

for letter in enumerate(letters):
    print(letter, end=" ")
print()
print("-" * 60)

for letter in enumerate(letters):
    print(letter[0], letter[1])
print("-" * 60)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"my_list :{my_list}")
print("-" * 60)

for lst in my_list:
    print(lst)
print("-" * 60)

for ind, lst in enumerate(my_list):
    print(f"{ind}\t{lst}")
print("-" * 60)

for ind, lst in  enumerate(my_list):
    print(f"list({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")
print("-" * 60)
