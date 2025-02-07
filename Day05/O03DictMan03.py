
print("update".center(60, "-"))
emp1 ={'name': 'Mike', 'age': 32, 'desig': 'TL', 'dept': 'MKT', 'loc': 'del'}
emp2 = {'name': 'John', 'age': 28, 'desig': 'SE', 'dept' : 'IT', 'salary': 125000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 60)
emp1.update(emp2)

print(f"emp1 :{emp1}")

print("pop".center(60, "-"))
emp1 = {'name': 'John', 'age': 28, 'desig': 'SE', 'dept': 'IT', 'loc': 'del', 'salary': 125000}
print(f"emp1 :{emp1}")

res = emp1.pop('desig')
print(f"res :{res}")

res = emp1.pop('loc')
print(f"res :{res}")

# res = emp1.pop()
# print(f"res :{res}")

print(f"emp1 :{emp1}")

print("popitem".center(60, "-"))
emp1 = {'name': 'John', 'age': 28, 'desig': 'SE', 'dept': 'IT', 'loc': 'del', 'salary': 125000}
print(f"emp1 :{emp1}")

res = emp1.popitem()
print(f"res :{res}")

res = emp1.popitem()
print(f"res :{res}")

print(f"emp1 :{emp1}")

