d = {}

d[100] = 'damodar'
d[200] = 'Niket '
d[300] = 'Tanmay'
d[400] = 'Aditya'
d['Buttya'] = 'Adesh'
print(d)
print(d.keys())
print(d.values())
'''
d={}
n = int(input("Enter the number of students"))

i=1
while i<n:
    name=input("Enter the name of student")
    marks=float(input("Enter the marks"))

    d[name] = marks
    i+=1


for i in d:
    print("\t" , i ," \t\t" , d[i])
'''

d[700]='vaibhav'
print(d)
del d[300]
print(d)

d.clear()
print(d)



d[100] = 'damodar'
d[200] = 'Niket '
d[300] = 'Tanmay'
d[400] = 'Aditya'
d['Buttya'] = 'Adesh'

print(d)


list=["a",98,4.8,'fhf']
d[600]=list

print(d)


t=1,2,3,4,
d[700]=t
print(d)

s={90,100,456}
d[800] = s
print(d)

dd={1:11,2:22}
d[900]=dd
print(d)
