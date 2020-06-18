import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

print(source)#it will provide output in form of string
data = json.loads(source)

daa=json.dumps(data,indent=2)

for item in daa['list']['resources']:
    print(item)
