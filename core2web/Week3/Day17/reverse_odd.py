'''Write a Program to that prints series of odd numbers in reverse order from the limiting number entered by user.
Input: 100
Output: 99 97 95 93 . . .. 1 '''


num=int(input("Enter the Number"));

for i in range(num-1,0,-2):

        print(i)
