n=int( input("Enter 1 for string 2 for number"))

s=input("Enter the string")
num = int(input("ERnter the number"));

d={}
d[1]=s
d[2] = num
for i in d:
    print(i , d[i])


'''num = input(" Enter 1 for string and 2 for Number");

if num == 1:

   str = input("Enter the String");
   print(str)

else:
    n = input("Enter the number")
    print(n)



n = input("Enter the number")
n = int(n)
for i in range(1, n+1,4):
    print(i , end=" ")


num = eval(input("Enter the number"))
s=c=0 ;
for i in range(1,num+1):
    if i % 2 == 0:
       s = i*i
       print(s , end=" ")
    else:
       c= i*i*i;
       print(c , end=" ")

num = 1
for i in range(1,5):
    for j in range(1,i+1):
          print(num , end=" ")
          num+=1
    print()
'''
num = int(input("Enter the number"))

for i in range(1,num+1):
    fact = 1

    for j in range(1,i+i):
        fact = fact *j

    print(fact)
