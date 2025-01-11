#json 읽기

import json

with open('c:/test/abc.json', 'r') as f:
    info = json.load(f)
print(info)

for i in info:
    print(i)
    for k, v in i.items():
        print(k, v)
    print('-'*30)