
FL = open("emp.csv", "r")

tsal = 0
FL.readline()       # Skip the header

for line in FL.readlines():
    sal = line.split(",")[4].strip()
    tsal += int(sal)

print(f"The total salary of all employees is {tsal}")

FL.close()