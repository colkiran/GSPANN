
def outerFun():
    gname = "Sachin"
    def innerFun():

        nonlocal gname              # only local var can be converted to nonlocal
        gname = "Rahul Dravid"
        print("hello world")
        print(f"Greetings Mr.{gname}")

    innerFun()
    print(f"outerFun :{gname}")

outerFun()
