
"""
read mode is the default mode of opening a file, if we don't specify the mode then it will open in read mode.
"""
FL = open("data.txt", "r")

# read() method reads the entire file and returns the content as a string.
# st = FL.read()

# read(n) method reads the n characters from the file and returns the content as a string.
# st = FL.read(100)

# readline() method reads the first line of the file and returns the content as a string.
# st = FL.readline()

# st = FL.readline(800)

# readlines() method reads the entire file and returns the content as a list of strings.
# st = FL.readlines()
# # print(st)
# for line in st:
#     print(line)

# readlines(n) method reads the entire paragraph where the 10th byte falls and returns the content as a list of strings.
st = FL.readlines(900)
print(st)

FL.close()