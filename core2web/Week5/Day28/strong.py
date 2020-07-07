'''Write a Program to check whether the entered number is Strong Number or Not.
{Note: A number can be termed as strong number; if the sum of factorials
 of each digit from that number is equal to that number, itself. e.g. 145 is a Strong Number since 1 + 24 + 120 = 145.}
 '''


'''
num=int(input("Enter the number"));
fact1=1;
fact=1
for i in range(2,100):
     fact=fact*i
     fact1=fact1+fact
     while(fact1<=num):
         if fact1==num:
             print("{} is strong number".format(fact1))
    '''


num=int(input("Enter the number"));
rem = 0
sum1 = 0
fact = 1
temp = num

while num!=0:
    rem = num%10
    fact =1
    for itr in range(2,rem+1):
        fact = fact*itr

    sum1 = sum1+fact
    num = num/10

if sum1==temp:
    print("The number is Strong number")
else:
    print("The number is not Strong")
