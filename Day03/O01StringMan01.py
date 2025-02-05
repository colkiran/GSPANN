
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(st)
print(f"st[0] :{st[0]}")         # indexing
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing
print(f"st[0:5:1] :{st[0:5:1]}")
print(f"st[6:11]  :{st[6:11]}")
print(f"st[0:11]  :{st[0:11]}")
print(f"st[0:11:2] :{st[0:11:2]}")
print(f"st[0:]    :{st[0:]}")
print(f"st[:11]   :{st[:11]}")
print(f"st[:]     :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
# slicing
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 60)
st = "malayalam"
print("Palidrome" if st[:] == st[::-1] else "Not a Palindrome")

print("-" * 60)
# strings are immutable
st = "hello world"
print(f"st :{st}")
print(f"st[0] :{st[0]}")
# st[0] = "H"

# not able to update the string  => immutable
# print(dir(st))
print("replace".center(60, "-"))
print(f"st :{st}")
res = st.replace("h", "H")
print(f"res :{res}")

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

res = st[:6] + st[6:].replace("l", "L")
print(f"res:{res}")

print("stirp".center(60, "-"))
st = "******hello******"
print(f"st: {st}")
print(st.lstrip("*"))
print(st.rstrip("*"))
print(st.strip("*"))