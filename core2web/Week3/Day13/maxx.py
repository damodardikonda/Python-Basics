'''

Write a Program that accepts Three integers from user and prints maximum number from them.
Input: 56 7  99
Output: The Maximum number amongst 56 7 & 99 is 99
'''

num1=int(input("enter the num1"));
num2=int(input("enter the num2"));
num3=int(input("enter the num3"));

if num1>num2>num3:
    print("num1 is greater")
elif num2>num1>num3:
    print("num2 is greater")
else:
    print("num3 is greater")
