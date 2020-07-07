''': Write a Program to takes a number from user and prints those digits who are prime in nature.
Input: 16532
Output: The Prime Digits are 1 5 3 2 '''


num=int(input("Enter the number"))

rem=0;

while n!=0:
    rem=num%10;
    for i in range(0,rem-1):

        if rem%1==0 and rem%rem==0:
            print(rem)

    num=num/10;
