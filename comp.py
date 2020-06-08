list=[1,4,2,5,6,22,45,66,33,4,9,8]

my_l=[]

#for n in list:
#    my_l.append(n)
#print(my_l)

#list comprehension for this is

#myli=[n for n in list]
#print(myli)

#myli=[n*n for n in list]
#print(myli)


m=map(lambda n:n*n,list)
print(m)

#list comprehension for printing even numbers

eve=[n for  n in list if n%2==0]
print(eve)

myl=filter(lambda n:  n%2==0,list )
print(myl)

#printing a0 b1 c2.. from abcd and 0,123

mylll=[(i,j) for i in range(4) for j in 'Abcd']
print(mylll)


name=['Rogers','Banner','Stark','Romanoff','Thor']
hero=['Capt America','hulk','Iron Man','Widow','Thundar god']
#zip method return a tuple of name and hero
print(zip(name,hero))


#for dictionary i want a zip file for name as akey and hero as value

mydict={}
for n,m in zip(name,hero):
    mydict[n]=m

print(mydict)

#comprehension through

mm={n:m for n,m in zip(name,hero) if name!='romanoff'}
print(mm)

mu=[1,2,2,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5]

sett={n for n in mu}
print(sett)
