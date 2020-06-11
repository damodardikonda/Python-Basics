tuple1=('a','b','c','d','e','f')
t2=tuple1

print(tuple1)
print(t2)


#tuple is not modified
#tuple1[0]='zam'
#print(tuple1)
#print(t2)


#set

set1={"science","math","eng","history"}
set2={"science","math","art","design"}
print(set1)#it never print in linear order and it avoid repeated value

print(set1.intersection(set2))

print(set1.difference(set2))

print(set1.union(set2))
print("science" in set1)

print(set1-set2)

print(set1| set2)
print(set1&set2)
set1.add('Dscience')
print(set1)

set1.update(set('as'))
print(set1)
set1.remove('math')
print(set1)

for item in set1:print(item*3)

print({1,2,3}.issubset(range(-5,5)))
