"""
write into a file - if the file already exists then it will delete the contents of the existing file and write newly into the file.
if the file doesn't exist then it will create a new file and write into it.
"""

FL = open("Myfile.txt", "w")
# st = input("Enter the content to write into the file: ")
# FL.write(st)

l1 = "This is the first line.\n"
l2 = "This is the second line.\n"
l3 = "This is the third line.\n"

FL.writelines([l1, l2, l3])
FL.close()