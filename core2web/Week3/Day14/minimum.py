'''
Write a Program that accepts Three integers from user and prints minimum number from them.
Input: 56 7  99
Output: The Minimum number amongst 56 7 & 99 is 7 '''


n1=int(input("enter the number"));
n2=int(input("enter the number"));
n3=int(input("enter the number"));

if n1>n2>n3:
    print("n1 is greater");
elif n2>n1>n3:
    print("n2 is greater");
else:
    print("n3 is greater")
