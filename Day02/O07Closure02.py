
def outerFun(greet):

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun

outerFun("Hello")("Sachin")

print("-" * 60)
engGrt = outerFun("Hello")
hndGrt = outerFun("Namaskar")


engGrt("Virat")
hndGrt("Jadeja")
