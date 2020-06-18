# javascript object notation

import json

people_string='''
{
   "people":[
   {
   "name":"Damodar Dikonda",
   "Phone":"9011738",
   "emails":["damodar5dikonda@gmail.com","damodar2dikonda@gmail.com"],
   "has_licensed": false

   },
   {
      "name":"Dams Dikonda",
      "Phone":"7744864",
      "emails":null,
      "has_licensed": true

   }



   ]
}'''

data=json.loads(people_string)
print(data)

#print("if you want to print the full information of person")
#for person in data['people']:
#    print(person)

#print("\n\n only name of peoples")
#for n in data['people']:
#    print(n['name'])

#print(type(data))
#print(type(data['people']))
#object           	dict
#array	            list
#string	             str
#number(int)	         int
#number(real)	    float
#true	             True
#false             	False
#null             	None


#dumps():=the dumps() is used to convert a data innto string, etc, .


print("\n now we want to delete a phone number and save it into new file which store it into string format");

for i in data['people']:
    del i['Phone']

new_string=json.dumps(data,indent=2,sort_keys=True)#indent is used for giving space
#sort_keys is used for printing in ascending order
print(new_string)
