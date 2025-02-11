"""
self will have the name of the object which made a call to the method

ply1.get_detials()      # self will have ply1 stored in it

"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 35)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 32)
ply2.get_details()

print("-" * 60)
# every object stores the instance variable data in a dictionary __dict__
print("ply1 :",  ply1.__dict__)
print("-" * 60)
print("ply2 :", ply2.__dict__)
ply2.runs = 140
print("ply2 :", ply2.__dict__)
print("-" * 60)
print("ply1 :",  ply1.__dict__)

