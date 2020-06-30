'''
 Write a Program which detects whether the entered number is perfect or not .
{Note: If sum of perfect divisors of number is equal to the entered number than it is considered as perfect one.}
Input : 6
Output : 6 is a Perfect number. '''

num=int(input("Enter the Number"));
sum=0;

for i in range(1,num/2+1):
    if num%2==0:
        sum=sum+i


if(num==sum):
    print("{} is perfect Number".format(num))
else:
    print("{} is not a perfect number".format(num))    
