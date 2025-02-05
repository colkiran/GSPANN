# conversions
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("-" * 60)
print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=362392394812))

print("-" * 60)
# alignment
print("{num:10} Tendulkar".format(num=36))
print("{num:10} Tendulkar".format(num="Sachin"))
print("{num:>15} Tendulkar".format(num="Sachin"))    # right
print("{num:^15} Tendulkar".format(num="Sachin"))    # center
print("{num:<15} Tendulkar".format(num="Sachin"))    # left
print("{num:-^60}".format(num="Sachin"))
print("Sachin".center(60, "-"))

print("-" * 60)
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 60)
print("{0:10.2f}\n{1:10.2f}".format(pi, -pi))
