import datetime


import json
with open("weekfile\Sat Feb 17 2024 18_58_25 GMT+0530 (India Standard Time).txt",'r',encoding='utf-8') as file:
 
    data = json.load(file)

keyfreq = {}

for item in data:
    if 'adx_keywords' in item:
        keywords = item['adx_keywords'].split(';')
        for a in keywords:
            keyfreq[a] = keyfreq.get(a, 0) + 1

keylist = dict(sorted(keyfreq.items(), key=lambda item: item[1], reverse=True))

print(keylist)

a= str(datetime.date.today())+'.json'
       
with open(f'{a}', 'w', encoding='utf-8') as outfile:
    json.dump(keylist, outfile, indent=4)

print("Done")
