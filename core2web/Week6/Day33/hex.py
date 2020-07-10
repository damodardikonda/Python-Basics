'''
Write a Program that prints Hexadecimal value of Each Digit from entered Number.
Input: 12
Output:
Binary of 1: 1
Binary of 2: 2

'''
num=int(input("Enter the Number"));
rem=0;

while num!=0:
    rem=num%10

    print(hex(rem))

    num=num//10
