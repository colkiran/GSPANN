
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun


engGrt = outerFun("Hello")

engGrtTgr = engGrt("tiger")

engGrtTgr("Junior NTR")



"""
engGrt = outerFun("Hello")
hndGrt = outerFun("Namaskar")

engGrtSngArw = engGrt("----->")
hndGrtSngArw = hndGrt("----->")

engGrtDblArw = engGrt("=====>>")


engGrtSngArw("Sachin")
hndGrtSngArw("Rohit")
engGrtDblArw("Virat")

"""
