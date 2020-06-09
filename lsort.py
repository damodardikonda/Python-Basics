li=[7,4,3,8,2,1,9,6,5]

s_li=sorted(li)

print("sorted list",s_li)# it createnew list but it does not sort previous list
print("original list",li)


li.sort()
print("editing previous list",li)

#sorted list in desending order
r_li=sorted(li,reverse=True)
print(r_li)

li.sort(reverse=True)
print(li)

# tuple doed  not have sort method

tup=(8,5,4,6,7,9,1,2,0,3)
s_t=sorted(tup)
print("sorted tuple",s_t)

dict={'name':'dame','age':30,'sal':34000}
di=sorted(dict)
print(di)

list=[-6,-4,-2,1,2,3]
lis=sorted(list)
print(lis)


#if we want to print 1,2,-2,3,4,-6
list=[-6,-4,-2,1,2,3]
lis=sorted(list,key=abs)
print(lis)


from operator import attrgetter

def emp():

    def __init__(self,name,age):
        self.name=name;
        self.age=age


    def __repr__(self):
        '({} is name and age is {})'.format(self.name,self.age)


e1=new emp('damodar',60000)
e2=new emp('dam',50000)
e3=new emp('damo',65000)

ee=[e1,e2,e3]
se=sorted(ee)
print(se, key=lambda x:x.name)

#print(se,key =attrgetter('age'))# it sort a object through age
