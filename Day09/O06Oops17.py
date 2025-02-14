
class Animal:

    def __init__(self):
        print(f"Animal Ctor.....")
        self.age = 1

    def eat(self):
        print("Animal eat....")

class Bird(Animal):

    def __init__(self):             # Overriding the parent Ctor
        super().__init__()          # calls the parent Ctor
        print("Bird Ctor.....")
        self.weight = '1 kg'

    def fly(self):
        print('Birds fly......')

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)
print(cuckoo.__dict__)

