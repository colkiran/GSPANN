
class Animal:

    def __init__(self):
        print("Animal Ctor...")
        self.a = 1

    def eat(self):
        print('Animals eat.....')


    def fun(self):
        print("method fun of Animal class....")

class Person:

    def __init__(self):
        print("Person Ctor......")
        self.p = 1

    def walk(self):
        print("Person walks.....")

    def fun(self):
        print("method fun of Person class....")

class Women(Animal, Person):

    def __init__(self):
        super().__init__()          # calls the parent Ctor
        Person.__init__(self)
        print("Women Ctor....")
        self.w = 1

    def talk(self):
        print("Women talks......")

sheela = Women()
sheela.talk()

print("-" * 60)
sheela.eat()
sheela.walk()

print("-" * 60)
sheela.fun()

print("-" * 60)
print(sheela.__dict__)