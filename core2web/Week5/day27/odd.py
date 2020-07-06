''' Write a Program to that accepts an integer value from user
and prints all odd numbers from that number to one using while loop.
Input: 65
 Output: 65 63 61 59 57 53 51. ....1

'''

num=int(input("Enter the Number"));

while num<=0:
    if num%2==0:
        print(num) 
