
def fun(*args):
    print(args, "\t", *args)

fun()
fun(10)
fun(10, 20)
fun(10, 20, 30)
fun(10, 20, 30, 40)
fun(200)
print("-" * 60)

def sum(x, y):
    print(f"Adding {x} and {y}")
    return x + y

def diff(x, y):
    print(f"Subtracting {y} from {x}")
    return x - y


# HOF - Higher Order Function
def log_Detials(fnc):
    logInfo = "Logging into a service"

    def helper(*args):
        print(logInfo)
        print(fnc(*args))           # call back
        print("Logging out of the service.......")
        print("-" * 60)

    return helper

sumLogger = log_Detials(sum)
sumLogger(50, 80)

diffLogger = log_Detials(diff)
diffLogger(70, 23)

