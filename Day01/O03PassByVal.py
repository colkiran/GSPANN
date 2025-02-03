
def fun(x):
    print(f"x inside fun :{x}")
    x = x + 100
    print(f"x inside fun :{x}")

y = 250

print(f"y before  :{y}")

fun(y)

print(f"y after :{y}")
