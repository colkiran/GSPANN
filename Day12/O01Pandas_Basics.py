
import pandas as pd

myData = {
    'emp' :['Jack', 'Jill', 'Robert', 'Kevin'],
    'dept':['MKT', 'HR', 'Finanace', 'Networking']
}

print(f'mydata :{myData}')

print("-" * 60)
empDF = pd.DataFrame(myData)
print(empDF)

print("-" * 60)
print(pd.__version__)

l1 = list(range(1, 6))
print(f"l1 :{l1}")

numSrs = pd.Series(l1)
print(numSrs)
print(type(numSrs))

print("-" * 60)
steps = {'day1': 3500, 'day2': 4500, 'day3': 5000, 'day4': 4800, 'day5': 6750}
print(f"steps :{steps}")

print("-" * 60)
myDF = pd.Series(steps, index=['day1', 'day2', 'day3', 'day4'])
print(f"myDf \n{myDF}")

print("-" * 60)
data = {
    'cars': ['audi', 'bmw', 'merc', 'jaguar'],
    'topspeed': [245, 270, 320, 310]
}

print(f"data :{data}")

print("-" * 60)
carDF = pd.DataFrame(data)
print(carDF)

print("-" * 60)
print(carDF.loc[2])

print("-" * 60)
print(carDF.loc[[0, 1]])

carDF.to_csv("cars.csv")
carDF.to_json("cars.json", indent=4)
