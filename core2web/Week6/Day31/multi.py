'''
Write a Program to that accepts a number from user print
multiplication of all Even Digits from that number.
Input: 1234
 Output: The Multiplication of all Even Digits is 8

'''

num=int(input("Enter the number"));
rem=0;
sum=1;
div=0;
while(num>0):
    rem=rem%10;
    num=num//10;
    if(num%2==0):
        sum=sum*num

print(sum)
