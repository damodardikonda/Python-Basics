'''Write a Program to that prints the series which increases with the number entered by user.
Input: 15
Output: 1 16  31  46 . . .. '''

num=int(input("Enter The Number"));

for i in (0,11):

    print(num*i+1)
    i+=1
