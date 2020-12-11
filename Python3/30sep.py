'''
from array import *

arr = array('i' ,[1789 , 2035 ,1899 , 2013 , 1458 , 2458 ,1254 , 1472 , 2365]);

for i in arr:
    if i == 2013 :
        print('found')
    elif i == 2015:
        print(" found")
    else:
        print("Not founfd")


my_arr = array('i' , [25 ,14,56,15,36,56,77,18,29])

for i in range(0,9):
    if(my_arr[i] == 25):
        print(i)
    elif my_arr[i] == 77:
        print(i)



import array

n = int(input("Enter the students count"))
a=[]
for i in range(n):

    a.append(int(input("Enter element")))

marks = array.array('i' , a)
sum=0
for i in range(n):
    sum = sum+ marks[i]
print(sum)



import array

n= int(input("Enter the number"))

a=[]

for i in range(n):
    a.append(int(input("Enter age")))

age = array.array('i',a)
temp = age[0]
for i in range(1,n):
    if age[i] > temp:
        temp = age[i]

print("Maximum range is " , temp)

'''


import array

n= int(input("Enter the number"))

a=[]

for i in range(n):
    a.append(int(input("Enter age")))

num = array.array('i',a)

for i in range(1,n):
    if num[i] > 0:
        print("positive")
    elif num[i] < 0:
        print("Negetive")
    elif num[i] % 2 == 0:
        print("even")
    elif num[i] == 0:
        print("Zero")
