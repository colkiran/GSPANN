
"""
read mode is the default mode of opening a file, if we don't specify the mode then it will open in read mode.
"""
FL = open("data.txt", "r")

# read() method reads the entire file and returns the content as a string.
st = FL.read()
print(st)


FL.close()