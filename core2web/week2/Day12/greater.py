''': Write a Program that accepts Two integers from user and prints maximum number from them.
Input: 56  99
Output: The Maximum number amongst 56 & 99 is 99 '''


#n1,n2=[int(i) for i in input("Enter the numbers:-")]

#if n1>n2:
#    print("{} is greater then {}".format(n1,n2))
#else:
#        print("{} is greater then {}".format(n2,n1))

try:
     num1=int(input("Enter the first number"));
     num2=int(input("Enter the first number"));

except ValueError as ve:
    print("enter the proper number")
    pass


if num1>num2:
    print("{} is greater then {}".format(num1,num2))
else:
        print("{} is greater then {}".format(num1,num2))
