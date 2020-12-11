from itertools import filterfalse


tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('a', 'b', 'c', 'd', 'e')
tuple3=cmp(tuple1,tuple2)
print(tuple3)
num = [1,2,3,4,5,6,7,8]

def is_even(n):
     return n%2==0
even = list(filterfalse(is_even,num))

print(even)


num = [1,2,3,4,5,6,7,8]

def is_even(n):

     return n%2==0
even = list(filter(is_even,num))

print(even)



num = [1,2,3,4,5,6,7,8]

def is_even(n):

     return n%2==0
even = tuple(filter(is_even,num))

print(even)

'''
num
print(list(filter([1,2,3,4,5,6,7,8,[],'a',0],num)))
'''
