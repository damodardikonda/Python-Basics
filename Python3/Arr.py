from array import *
'''
arr = array('i' , [20,30,40,50,60])
for i in range(1N,5):
    print(arr[i])

print("$$$$$$$$$$" *4)


hard_arr = array('i' ,[])
hard_arr.append(10)
hard_arr.append(20)
hard_arr.append(35)
hard_arr.append(40)
hard_arr.insert(2,80)
hard_arr.insert(0,23)
hard_arr.insert(3,999)

for i in hard_arr:
    print(i)
print("**********" * 2)
for i in hard_arr:
    if i % 2 == 0:
        print(i)



float_arr = array ('d' , [78.567 , 23.697 ,78.34 ,90,12])
float_arr.append(12.456)
float_arr.insert(3,76.34)

avg = 0
sum = 0
count = 0
for i in float_arr:
    sum = sum + i
    count+=1

avg = sum /count
print("average is " + str(avg))


a  = array('u' ,('A','B','C',"D" ,'E'))

for i in range(0,5):
    for j in range(i,5):
        print(a[j] , end=" ")
    print()


'''
import numpy as np

str_arr = ["Damodar" ," Bhaskar" ,"Dikonda" ,"Hiii"]
arr = np.array(str_arr)
for i in arr:
    print(i)
