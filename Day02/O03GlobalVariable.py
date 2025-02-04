
glbX = 100

def fun(y):
    # do not assign any value in the below line
    global glbX
    print(f"inside fun :{y}")
    glbX = 300
    print(f"inside fun :{glbX}")


print(f"before call to fun :{glbX}")

fun(10)

print(f"after call to fun :{glbX}")

