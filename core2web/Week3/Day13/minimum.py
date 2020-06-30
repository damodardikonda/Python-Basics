'''Write a Program that accepts Two integers from user and prints minimum number from them.
Input: 56  99
Output: The Minimum number amongst 56 & 99 is 56 '''


#num1=int(input("Enter the Number:="));
#num2=int(input("Enter the Number2:="));

#if num1>num2:
#    print("{} is Minimum then {} ".format(num2,num1));
#else:
#        print("{} is minimum then {} ".format(num1,num2));



#num1,num2=[int(i) for  i in input("Enter the number:=").split()]


#if num1>num2:
#    print("{} is Minimum then {} ".format(num2,num1));
#else:
#        print("{} is minimum then {} ".format(num1,num2));

try:
    num1,num2=[int(i) for  i in input("Enter the number:=").split()]
except valueError as ve:
    print("Enter the invalid number");
    pass

if num1>num2:
    print("{} is Minimum then {} ".format(num2,num1));
else:
        print("{} is minimum then {} ".format(num1,num2));
