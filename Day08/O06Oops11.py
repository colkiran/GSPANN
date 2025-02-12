
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular JS', 'React JS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val


emp1 = Employee("Mike", 30000)
print(emp1)

print("-" * 60)
emp2 = Employee("Kevin", 50000)
print(emp2)

print("-" * 60)
print(len(emp1))

print("-" * 60)
res = [t for t in emp1]
print(res)

print("-" * 60)
emp1.append("Python")

res = [t for t in emp1]
print(res)

print("-" * 60)
x = emp1[2]
print(x)

print("-" * 60)
# immutable object converted to mutable
res = [t for t in emp1]
print(res)

emp1[2] = 'JSP'

res = [t for t in emp1]
print(res)
