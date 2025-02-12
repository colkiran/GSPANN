
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # works for not equal to also
    def __eq__(self, other):
        return self.salary == other.salary

    # works for less than also
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("John", 80000)
print(emp1)

print("-" * 60)
emp2 = Employee("Peter", 70000)
print(emp2)

print("-" * 60)
# emp1 == emp2  - it should be comparing on the salaries of the employee
if emp1 != emp2:
    print("{}'s salary of {} is not equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
if emp1 > emp2:
    print("{}'s salary of {} is greater than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is less than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
print(emp1 >= emp2)
