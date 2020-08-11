num1=200;
num2=600;

for i in range(num1,num2):
   sqrt=i;
   temp=0;
   while(sqrt!=temp):
       temp=sqrt
       sqrt=(((i/temp)+temp)%10);

   print(sqrt,end=" ");
'''


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
for i in range(num1, num2 + 1):
    sqrt = i / 2# 113
    temp = 0
    while(sqrt != temp):#
        temp = sqrt#113
        sqrt = (((i / temp) + temp) / 2)#

    print(sqrt, end = " ")
'''
