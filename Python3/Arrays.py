from array import *
'''
my_arr = array('i' , [1,2,3,4,5])
print("1 st elemnt "+str(my_arr[0]))

print("\n\nlast Element")
print(my_arr[4])
''


my_arr = array('b',[1,2,127,-1,-129])
print(my_arr)


my_arr = array('B',[1,2,127,128,256])
print(my_arr)


my_arr = array('c',['a','b','c'])
print(my_arr)

a = array( [456,-3000,123])
print(a)

'''
#print(" append() method")
'''
a = array('d', [45.8900,-300,300,123,])
a.append(10)

print("Insert Method")
a.insert(2,67)
print(a)
''


print("Extend Method")

abc = array('i',[1,2,3,4])
de = array('i',[5,6,7])
abc.extend(de)
print(abc)



abc = array('i',[1,2,3,4])
de = array('i',[5,2,3])
abc.extend(de)
print(abc)



abc = array('f',[1.8,2.5,3.7,4.2])
de = array('d',[5.7,6.9,7])
abc.extend(de)
print(abc)


''

print(" Add item from list into array using fromlist() method")
a = array('i', [1,2,3,4])
b = [2,3,4]

a.fromlist(b)
print(a)

a = array('i', [1,2,3,4])
b = [2.0,3.5,4.7]

a.fromlist(b)
print(a)
''

print("Remove method")

my_array = array('i', [2,4,5,6,10,20])
my_array.remove(4)
print(my_array)
'''

my_array = array('i', [10,20,5,40,50])
print(my_array.index(5))


abc = array('u', ['g','e','e','k'])
abc.fromstring("stuff")
print(abc)
