# javascript object notation
#write json into file and vise versa
import json

print("loading a json file into python")

with open('states.json') as f:
    data=json.load(f)#data is nothing but python object


for st in data["states"]:
    print(st['name'], st['abbreviation'])


#dump() convert data into json file
for delete in data["states"]:
    del delete['abbreviation']

with open ('new_file.json','w') as f:
json.dump(data ,f, indent=2)
print(new_file)
