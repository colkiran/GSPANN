
class Player:           # pascal casing

    def getruns(self):
        print(self.__class__)
        print(f"runs scored.....")

sachin = Player()
sachin.getruns()

print("-" * 60)
print(type(sachin))

print("-" * 60)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))