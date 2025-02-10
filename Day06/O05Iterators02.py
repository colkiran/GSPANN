lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"lst :{lst}")

iterObj = lst.__iter__()

while True:
    try:
        elem = next(iterObj)
        print(elem)
    except StopIteration:
        break
