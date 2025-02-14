
class MyStr(str):

    def AppenMr(self):
        return "Mr." + self

st = MyStr("Rahul")
print(st.AppenMr())

print("-" * 60)

class MyListClass(list):

    def append(self, object):
        super().append(object)

l1 = MyListClass()
print(f"l1 :{l1}")
print(type(l1))

l1.append("Sachin")
l1.append("Sourav")
l1.append("Rahul")

print(l1)
