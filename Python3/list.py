list = [1,2,32,43,89]
'''
i = 0
while  i < len(list):
    print(list[i])
    i = i +1

i = len(list)
for x in range(i):
    print(x-i)# print negetive index
'''
list.append(100);
list.append(2);
list.append(1);
print(list)


'''list.append(100,46,59);
print(list)
'''

a = [1,2,3,4]
b = [9,56]

print(id(a))
a= a + b + [9,56]

print(id(b))


ab=[1,2,3,50,100]
ab.insert(10,20)
print(ab)

print(ab.index(20))

ab.remove(100)
print(ab)


aa = [20,50,1,2,4,90,76,55]
aa = aa.sort()
print(aa)

bb = ['A','a','b','B','C']
bb.sort();
print(bb)


c= [1,2,3]
print(id(c))
c= c* 3
print(id(c))
print(c)

cc=[[1,2,3],[4,5,6]]*3
print(cc)

a1 = [1,2,3]
b1 = a1
a1.append(78);
print(b1)


a2 = [10,202,30]
b2=list(a2)
a2.append(89)
print(b2)
