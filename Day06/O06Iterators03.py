class Mynumbers:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            res = self.n
            self.n += 2
            return res
        else:
            return StopIteration

myOjb = Mynumbers(5)
iterObj = myOjb.__iter__()

print(myOjb.__next__())
print(next(myOjb))
print(myOjb.__next__())
# print(myOjb.__next__())
# print(myOjb.__next__())
# print(myOjb.__next__())



