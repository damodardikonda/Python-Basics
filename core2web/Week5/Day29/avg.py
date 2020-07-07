'''Write a Program to that accepts an integer value
 from user and prints the Average of all the
 Input: 1234
 Output: The Average of digits from number 1234 is 5
 '''


num=int(input("Enter the Number:="));

avg=0;
rem=0;
sum=0;
count=0

while num!=0:
    rem=num%10
    sum=sum+rem;

    num=num/10

    avg=int(sum/2)

print("Average of Entered number is"+str(avg))
