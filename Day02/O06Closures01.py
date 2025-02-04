
def outerFun():
    gname = "Sachin"
    def innerFun():

        print("Hello World")
        print(f"Greetings {gname}")

    return innerFun

outerFun()()        # calls the innerFun()

print("-" * 60)

inref = outerFun()
# after few lines of code

print("Hello World\n" * 5)

inref()     # call the innerFun