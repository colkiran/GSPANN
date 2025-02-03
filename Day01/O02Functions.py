
def greet():
    print("Greetings Mr. Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# city - default argument, gname - non default argument
def greetGstCty(gname, city = "Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.....")

greet()

print("-" * 60)

greetGst("Sourav")
greetGst("Yuvraj")

print("-" * 60)

greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
"""
functions takes arguments in two different ways
    a. arguments
    b. key word arguments (kwargs)
"""

def admission(fname, lname, dob, qlf, city, contno, gender, addr):
    print(f"fname :{fname}")
    print(f"lame :{lname}")
    print(f"Birthdate :{dob}")
    print(f"Qualification :{qlf}")
    print(f"Contact No. :{contno}")
    print(f"Gender :{gender}")
    print(f"addr :{addr}")

# args
admission('John', 'Slater', '23/09/1985', 'Btech', 'Delhi', '993242394', "Male", "MG road, 8th Cross, 1st main, Mumbai")

print("-" * 60)
# kwargs
admission(dob = '15/01/1981', fname= "Kevin", addr = "Door No 144, 10th cross, 5th Main, Mumbai", city= 'Mumbai', lname ='Peterson', qlf='Graduate', gender='Male', contno='245645632')

print("-" * 60)
# Variable length Arguments
# *numbers - can accept more than one value and store it in a tuple or lst
def prodOf(*numbers):
    print(numbers)
    print(*numbers)         # unpack the list, [] and , will disappear
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print(prodOf(1, 2, 3, 4, 5))

print("-" * 60)
# ** before a variable it accepts data in a dictionary
def extractDetails(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

extractDetails(name='Sachin', runs=120, oponent='AUS', venue='Perth')

print("-" * 60)
# return

def addMe(x, y):
    return x + y

print(f"The sum of 10 and 20 is :{addMe(10, 20)}")

print("-" * 60)

def arithmetic(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmetic(30, 12)
print(res)

print("-" * 60)

def fun():
    "This is doc string"
    #This is a comment
    print("Hello World")

fun()

print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1
    takes two arguments x and y

    1. if x and y are numbers then we get the sum of the numbers
    2. if x and y are string then we get a concatenated string as output
    3. if x and y are two different data types then we get an error
    """
    return x + y

print(fun1(100, 200))
print(fun1("hello ", "world"))
# print(fun1(100, 'hello'))

print("-" * 60)
help(fun1)
