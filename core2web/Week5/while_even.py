'''Write a Program to that accepts an integer value from user
 and prints all even numbers from that number to 0 using while loop.
 Input: 65
Output: 64 62 60 58 56 54 52 . . . .. 0

'''
n=int(input("Enter The Number"));

while n<0:
    if n%2==0:
        print(n)
