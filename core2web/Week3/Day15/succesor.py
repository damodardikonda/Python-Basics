''' Write a Program that accepts an integer from user and prints its second successor and second predecessor. '''

#num=int(input("Enter the number"));

#num1=num-2
#print("the predecasor is",num1)

#num2=num+2
#print("the Successor is",num2)

try:
    num=int(input("Enter the number"));
except ValueError as VE:
    print("ENter valid number");

num1=num-2
print("the predecasor is",num1)

num2=num+2
print("the Successor is",num2)
