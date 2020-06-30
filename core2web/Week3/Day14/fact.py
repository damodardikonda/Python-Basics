'''

Program 2: Write a Program that accepts Two integers from user and prints
 the series of factorial of all numbers between those two inputs.
Input: 1 to 5
Output:
 Factorial of 1 = 1
 .
 .
 Factorial of 5 = 120
 '''
fact=1

#num1,num2=[int(i) for i in input("Enter the Number:-").split()]
#for i in range(num1,num2):
#    fact=fact*i
#    print("Factorial of {} is {}".format(i,fact));
#    i+=1;


num1=int(input("Enter the Number"));
num2=int(input("Enter the number2"));
for i in range(num1,num2):
    fact=fact*i
    print("Factorial of {} is {}".format(i,fact));
    i+=1;
