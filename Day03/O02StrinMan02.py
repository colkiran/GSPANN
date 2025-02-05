
"""
maketrans, translate
"""

print("maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")
a = 'helowrd'
b = 'HELOWRD'

# length of a and b should be the same
res_tbl = st.maketrans(a, b)
print(f"result table :{res_tbl}")

print("translate".center(60, "-"))
res = st.translate(res_tbl)
print(f"res :{res}")

print("formatting".center(60, "-"))
# c style of formatting
format = "Welcome %s, what a %s player"
print(format)

values = ("Sachin", "superb")
print(values)

print("-" * 60)
print(format, values)

print("-" * 60)
print(format % values)

print("-" * 60)
print("Welcome %s, what a %s player" % ("Sachin", "superb"))

print("-" * 60)
format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4.8, "class"))
print(format % ("Sachin", 4.763234, "class"))
print(format % ("Sachin", 4.7423123125, "class"))
print(format % ("Sachin", 4.8, "class"))

print("-" * 60)
# unix style formatting
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)

print(tmpl.substitute(name = "Sachin", adj = "class"))

print("-" * 60)
# string format in python

print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))

print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))

print("Welcome {2}, what a {0} player for {1}".format("Sachin", "class", "India"))

print("Welcome {pname}, what a {adj} player for {ctry}".format(pname="Sachin", adj="class", ctry="India"))

print("Welcome {pname}, with a rating {rating}, what a {adj} player".format(pname= "Sachin", adj="class", rating=4))

print("Welcome {pname}, with a rating {rating:.3f}, what a {adj} player".format(pname= "Sachin", adj="class", rating=4.89297323))

print("-" * 60)
# interpolation
from math import pi, e
print(f"PI = {pi} and Eulers constant = {e}")

print("PI={} and Eulers Constant = {}".format(pi, e))

print("PI={} and Eulers Constant = {} and magic number = {magic}".format(pi, e, magic=40585))

print("-" * 60)
full_name = ["Sachin", "Tendulkar"]
print(full_name)
print("Mr.{name}".format(name = full_name))
print("Mr.{name[0]} {name[1]}".format(name=full_name))
