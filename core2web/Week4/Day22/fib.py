'''
 Write a Program to print Fibonacci Series of N elements. Where n is
a number entered by user.
Output: 0 1 1 2 3 5 8 13 21 34
 '''

n=int(input("enter the number"))

#print("enter positive number") if n==-1 else print("Nice")

a=0
b=1
print(a,b)

for i in range(n-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
