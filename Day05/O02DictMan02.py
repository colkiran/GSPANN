
print("keys".center(60, "-"))
emp = {'name': 'Jack', 'age': 35, 'desig': 'MGR', 'dept': 'Finance', 'salary': 145000, 'loc': 'delhi'}
print(f"emp :{emp}")

k = emp.keys()
print(f"keys :{k}")

for k in emp.keys():
    print(k + " => " + str(emp[k]))

print("values".center(60, "-"))
emp = {'name': 'Jack', 'age': 35, 'desig': 'MGR', 'dept': 'Finance', 'salary': 145000, 'loc': 'delhi'}
print(f"emp :{emp}")

v = emp.values()
print(v)

print("items".center(60, "-"))
emp = {
    'emp1': {'name': 'Mike', 'age': 32, 'desig': 'TL', 'dept' : 'MKT', 'salary': 80000},
    'emp2': {'name': 'John', 'age': 28, 'desig': 'SE', 'dept' : 'IT', 'salary': 125000},
    'emp3': {'name': 'Slater', 'age': 30, 'desig': 'lead', 'dept' : 'testing', 'salary': 90000}
}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("get".center(60, "-"))
emp1 = {'name': 'Mike', 'age': 32, 'desig': 'TL', 'dept' : 'MKT', 'salary': 80000}

print(f"emp1 :{emp1}")
print(type(emp1))

print("-" * 60)

print(f"Name :{emp1.get('name', 'Invalid Key, plaease enter a valid key')}")
print(f"Desig :{emp1.get('desg', 'Invalid Key, plaease enter a valid key')}")

print("fromkeys".center(60, "-"))
# convert a list into a dictionary

cities = ['blr', 'che', 'hyd', 'pun', 'mum', 'del', 'kol']
print(f"cities :{cities}")

print("-" * 60)
res = dict.fromkeys(cities)
print(f"res :{res}")

print("-" * 60)
res = dict.fromkeys(cities, 23)
print(f"res :{res}")

print("setdefault".center(60, "-"))
emp1 = {'name': 'Mike', 'age': 32, 'desig': 'TL', 'dept' : 'MKT', 'salary': 80000}

print(f"emp1 :{emp1}")
emp1.setdefault('name', 'Tyson')
emp1.setdefault('desig', 'PM')
emp1.setdefault('loc', 'Hyd')
emp1.setdefault('gender', 'male')

print(f"emp1 :{emp1}")

