
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is :{self.name}\nSalary is :{self.salary}"

emp1 = Employee("Steve", 45000)
# emp1.get_details()

print("-" * 60)
print(str(emp1))

print("-" * 60)
print(emp1)             # implicitly call __str__