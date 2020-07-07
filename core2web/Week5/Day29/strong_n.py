''' Write a Program to print Series of Strong Numbers up to Nth Elements. Where n is the number entered by User'''

num=int(input("enter the number"))

rem=0
sum=0
temp=num
while n!=0:
    rem=rem%10
    fact=1

    for i in range(2,rem+1):
         fact=fact*i

         sum=sum+fact
         num=num/10


if sum==temp:
    print("it is strong number");
else:
    print("Number is not strong ")
