
def outerFun():
    gname = "Sachin"
    def innerFun():
        
        print("Hello World")
        print(f"Greetings {gname}")

    innerFun()

outerFun()
