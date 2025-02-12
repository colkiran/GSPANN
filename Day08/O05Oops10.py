
"""
Arithmetic Operators
1. add
2. sub
3. Mul
4. div
"""

class ArithCalc:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return ArithCalc("noName", self.salary + other.salary)

    def __sub__(self, other):
        return ArithCalc("noName", self.salary - other.salary)

    def __mul__(self, other):
        return ArithCalc("noName", self.salary * other.salary)

    def __truediv__(self, other):
        return ArithCalc("noName", self.salary / other.salary)



emp1 = ArithCalc("Jack", 30000)
emp2 = ArithCalc("Jill", 45000)
emp3 = ArithCalc("Tina", 50000)

print(emp1)
print("-" * 60)
print(emp2)
print("-" * 60)

print(f"add :{emp1 + emp2}")
print(f"add :{emp1 + emp2 + emp3}")

print("-" * 60)

print(f"sub :{emp2 - emp1}")

print("-" * 60)

print(f"mul :{emp1 * emp2}")

print("-" * 60)

print(f"div :{emp2 / emp1}")