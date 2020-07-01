'''Write a Program to Swap two entered number without using a third temporary variable.
Input: 10 30
Output:
Before Swap: a = 10 & b = 20
After Swap: a = 20 & b = 10 '''


num1=int(input("Enter the Number"));
num2=int(input("Enter the Number"));

print("Before swapping {} {}".format(num1,num2))

num1=num1+num2;
num2=num1-num2
num1=num1-num2

print("After swapping {} {}".format(num1,num2))
