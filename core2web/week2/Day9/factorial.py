'''Write a C program to calculate the factorial of a given number.
Input: 5
Output:
 The Factorial of 5 is: 120

 '''
try:
     a=int(input("enter the Number"))
except ValueError as ve:
    print("Enter proper value")
    pass
    exit(0)

fact=1

for i in range(2, a+1):
    fact=fact*i;


print(fact)




#num=5
#fact=1
#for i in range(fact,num+1):
#    fact=fact+i;
#print(fact)




# using if else case
#num=5
#fact=1
#if num>=0:
     #for i in range(fact,num+1):
          # fact=fact+i;
#print(fact)

#else:print("Enter the proper number")
