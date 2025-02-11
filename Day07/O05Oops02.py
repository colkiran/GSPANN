
class Player:

    def __init__(self):           # constructor
        print('Player Initialized....')

    def get_runs(self):
        print(f"runs scored.....")

    def __del__(self):              # destructor
        print("destroying the object.....")


sachin = Player()           # calls the constructor
sourav = Player()
sachin.__init__()

print("-" * 60)
sachin.get_runs()
sourav.get_runs()

print("-" * 60)
del sachin                  # calls the destructor
print("hello world \n" * 5)
