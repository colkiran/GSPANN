
# dictionary comprehension
lst = [1, 2, 3, 4, 5]
print(f"lst :{lst}")
sqrs = [x ** 2 for x in lst]
print(f"sqrs :{sqrs}")
print("-" * 60)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(f"dict1 :{dict1}")
print("-" * 60)

d1 = {item for item in dict1}
print(f"d1 :{d1}")
print("-" * 60)

d2 = {item for item in dict1.keys()}
print(f"d2 :{d2}")
print("-" * 60)

d3 = {item for item in dict1.values()}
print(f"d3 :{d3}")
print("-" * 60)

d4 = {k: v for k, v in dict1.items()}
print(f"d4 :{d4}")
print("-" * 60)

d5 = {k: v * 2 for k, v in dict1.items()}
print(f"d5 :{d5}")
print("-" * 60)

d6 = {v * 2: k for k, v in dict1.items()}
print(f"d6 :{d6}")
print("-" * 60)

players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

print(f"players :{players}")
print("-" * 60)

print(f"sachin :{players['sachin']}")
print("-" * 60)

print(f"sachin  :{sum(players['sachin'])}")
print("-" * 60)

scores = {k: sum(v) for k, v in players.items()}
print(f"scores :{scores}")
print("-" * 60)

scores = [player for player in players.keys()]
print(f"scores :{scores}")
print("-" * 60)

scores = [runs for runs in players.values()]
print(f"scores :{scores}")
print("-" * 60)

ply_scores = {k: (lambda scores: sum(scores) / len(scores))(v)
              for k, v in players.items()}
print(f'player scores :{ply_scores}')
print("-" * 60)

vals = [{x: (lambda par: "Mr." + par) ("sachin {}".format(x))}
        for x in range(1, 6)]
print(vals)
print("-" * 60)

vals = {(lambda par : par * 10)(k): (lambda par: par * par)(v)
        for k, v in {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}.items()}
print(vals)
print("-" * 60)

players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

scores = [ply_score for ply_score in players.values()]
print(f'scores :{scores}')
print("-" * 60)

scores = [x for ply_score in players.values() for x in ply_score if x > 200]
print(f"scores :{scores}")
print("-" * 60)

scores = [str(x) for ply_score in players.values() for x in ply_score if x > 200]
print(f"scores :{scores}")
print("-" * 60)

scores = {name: [scr for scr in score if scr >= 200]
          for name, score in players.items()}
print(f"Scores :{scores}")
