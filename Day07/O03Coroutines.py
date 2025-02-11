
def get_name(surname):
    print(f"Surname is :{surname}")
    while True:
        name = yield
        print(f"received {name}")
        if surname in name:
            print(f"surname match :{name}")

corou = get_name("tendulkar")
corou.__next__()

corou.send("ali")
print("-" * 60)
corou.send("peter")
print("-" * 60)
corou.send("mark")
print("-")
corou.send("tendulkar sachin")