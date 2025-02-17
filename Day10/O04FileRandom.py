
FL = open("data.txt", "rb")

pos = FL.tell()
print(f"pos :{pos}")

pos = FL.seek(85, 0)
print(f"pos :{pos}")

pos = FL.seek(48, 1)
print(f"pos :{pos}")

pos = FL.seek(100, 2)
print(f"pos :{pos}")

pos = FL.seek(-500, 2)
print(f"pos :{pos}")     # 3868

FL.close()

