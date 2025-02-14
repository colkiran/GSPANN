
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.age = 1

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def fly(self):
        print("birds fly.....")

class Fish(Animal):

    def swim(self):
        print("Fishes swim......")



cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()

print("-" * 60)

dolphin = Fish()
dolphin.swim()
dolphin.eat()

print("-" * 60)
print(f"Bird :{cuckoo.__dict__}")
print(f"Fish :{dolphin.__dict__}")
