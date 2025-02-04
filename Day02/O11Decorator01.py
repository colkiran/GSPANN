
def outerFun(fnc):

    def Helper(amt):
        print("Logging into the server......")
        fnc(amt)
        print("logging out of the server......")
        print("-" * 60)

    return Helper

def deposit(x):
    print(f"Amount {x} credited successfully into the account.....")

depositRef = outerFun(deposit)
depositRef(10000)

print("-" * 60)
@outerFun           # withdraw = outerFun(withdraw)
def withdraw(x):
    print(f"Amount {x} debited successfully from the account.....")

# withdraw = outerFun(withdraw)
# withdraw(3500)

withdraw(5000)      # calling the Helper Function

