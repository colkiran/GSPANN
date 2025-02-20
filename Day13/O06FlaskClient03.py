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

print('post'.center(60, "-"))
fanta = {'item': '200 ml bottle', 'price': 20, 'qty': 800}

response = requests.post(BASE + 'getproduct/fanta', json=json.dumps(fanta))
# print(response.json)

res = response.json()
print(res)
print("-" * 60)

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("delete".center(60, "-"))
response = requests.delete(BASE + 'getproduct/thumbs_up')
res = response.json()
print(res)
print("-" * 60)

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

