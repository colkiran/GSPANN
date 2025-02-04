
def fun(y):         # y is a local variable
    print(f"Inside fun :{y}")
    x = "Hello World"        # local variable
    print(x)

fun(100)

# print(f"Outside fun y :{y}")
# print(f"Outside fun x :{x}")
