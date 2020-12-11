import array
'''
a=[ ]
for i in range(0,3):
    a.append(int(input()))

rever = array.array('i',a)
for i in range(2,0):
    print(rever[i])


n = int(input("Enter the length "))
a=[]
for i in range(n):
    a.append(int(input()))

arr = array.array('i' ,a)

temp=arr[0]
print("FIrst number is " ,temp)

for i in range(1,n):
    if arr[i] > temp:
        temp = arr[i]

print("Greater number is" ,temp)


n = int(input("Enter No of overs"))

total_ball = n * 6

a = list()

for i in range(total_ball):
    a.append(int(input("Enter the Runs")))

run = array.array('i' , a)
score =six =four=other=dot = 0
for i in range(total_ball):
    score+=run[i]
    if(run[i] == 6):
        six+=1
    elif run[i] == 4:
        four+=1
    elif run[i] == 0:
        dot+=1
    else:
        other+=1
print("total ball is " ,total_ball )
print(" total Runs are = " , score)
print(" SIxes " , six )
print("Fours " , four)
print("Dot balls " , dot)
print("others" , other)


'''

a =[]
for i in range(0,5):
    a.append(int(input()))

arr1 = array.array('i' , a)
b =[]

for i in range(0,5):
    if arr1[i] % 2 == 0:
        b.append(-1)
    else:
        b.append(arr1[i])
arr2 = array.array('i' , b)
for i in range(0,5):
    print(arr2[i])
