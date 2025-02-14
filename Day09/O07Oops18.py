
class Animal:

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Chicken(Bird):

    def fly(self):
        print(f"Chickens seldom fly.....")

chic = Chicken()
chic.fly()
chic.eat()

