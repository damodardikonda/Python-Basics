'''
: Write a Program that takes a number as input from user and prints only those
 digits from that number, which are prime in nature.
Input: 141
 Output: The Prime Digits from the Number 141 is 1, 1.
 '''


num=int(input("Enter The Number:="));

sum=0
rem=0

while(num>0):
    rem=rem%10;
    num=num/10;

    if rem%1==0 and rem%rem==0:
        print(rem)

    else:
        print("Not a Prime Number");
