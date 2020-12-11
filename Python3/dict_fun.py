d = dict([(100,'Damodar'),(200,'Bhaskar'),(300,'Dikonda')])
print(d)

d=dict({(1,"AAA"),(2,"BBB"),(3,"CCC")})
print(d)

d=dict(((10,'Pune'),(20,"Mumbai"),(30,"Nashik")))
print(d)

print("length of dict " ,len(d))
print("value of 10 key is " , d.get(10))

print("the value of 500 is " ,d.get(500))

print(d.get(1000,'Delhi'))

d[400]="Nagpur"

print(d.pop(20))
print(d)

for k in d.keys():
    print(k)


for v in d.values():
    print(v)

for (k,v) in d.items():
   print(k," ",v)
