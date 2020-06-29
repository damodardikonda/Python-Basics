'''
Write a Program to print Cubes and Squares of all Even numbers ranges between given input number.
Input:  10
Output:
  Cube of 2 : 8 and Square of 2 : 4
    Cube of 4 : 64 and Square of 4 : 16
  .
  .
    Cube of 10 : 1000 and Square of 10 : 100 '''

num1=int(input("enter the number"))
num2=int(input("enter the number"))

for i in (1,num2+1):
    if i%2==0:
       Square=i*i
       cube=i*i*i
       print("Square of",i,Square);
       print("cube of",i,cube);
