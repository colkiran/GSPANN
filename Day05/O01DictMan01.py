
d1 = dict()
print(f'd1 :{d1}')
print(type(d1))

print("-" * 60)
d2 = {'name': 'sachin', 'age': 36, 'runs': 98, 'opponent': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'Rahul'), ('age', 32), ('runs', 80), ('opponent', 'Pak')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='Virat', age=35, runs=145, opponent='nzl')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD
# create
player = {'name': 'Sachin', 'age': 36, 'runs': 125, 'opponent': 'WI'}
print(f"player: {player}")

# read
print("-" * 60)
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
for x in player:
    # print(x, end=" ")
    print(x, "=>", player[x])

print("-" * 60)
# update - modify, add new key val
player['name'] = 'Tendulkar'
player['runs'] = 185
player['year'] = 2001
player['venue'] = 'Sabina Park'

print(f"player :{player}")

print("-" * 60)
# del
del player['age']
del[player['runs']]

print(f"player :{player}")

print("-" * 60)
print(dir(player))

