import json

import requests

BASE = "http://127.0.0.1:5000/"

print("GET".center(60,"-"))

response = requests.get(BASE + 'getproduct/pepsi')

res = response.json()

print(res)
print("-" * 60)

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("put".center(60, "-"))
response = requests.put(BASE + "getproduct/coke", data={'cat': 'baverage'})

res = response.json()

print(res)

print("-" * 60)

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("patch".center(60, "-"))
data = {'price': 5000}

response = requests.patch(BASE + 'getproduct/coke', json= json.dumps(data))
res =  response.json()

print(res)
print("-" * 60)

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)