
import requests

BASE = 'http://127.0.0.1:5000/'

respose = requests.get(BASE + 'getproduct/thumbs_up')

res = respose.json()

print(res)

print("-" * 60)
for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
