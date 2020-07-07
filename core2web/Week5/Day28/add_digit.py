'''Write a Program to that accepts an integer value from user
and prints the sum of all digits from that number.
 Input: 15895 Output: The sum digits from numbers 15895 is 28
'''

num=int(input("Enter the number"));
rem=0;
sum=0;


while num!=0:
    rem=num%10
    sum=int(sum+rem);


    num=num/10;

print("Sum is "+str(sum))
