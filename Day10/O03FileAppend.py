
"""
if the file is already exist, it will edit the file and write the content into it without disturbing the existing content.
if the file is not exist, it will create a new file and write the content into it.
"""

FA = open("Myfile.txt", "a")
st = input("Enter the content to write into the file: ")
FA.write(st + "\n")

FA.close()
