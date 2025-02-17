
import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)

for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 60)

print("-" * 60)
empdata = '{"name" : "Mike", "age": 29, "city": "New York"}'
print(empdata)
print(type(empdata))

# convert JSON string to Python dictionary
res = json.loads(empdata)
print(res)
print(type(res))
for k in res:
    print(k, "=>", res[k])