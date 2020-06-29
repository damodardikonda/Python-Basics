''' Write a Program which accepts two integers from user and swaps their insertion order.
 Input :  20 30
 Output :
Before Swap : 20 30
   After Swap : 30 20
 '''
#a=int(input("enter the number"))
#b=int(input("enter the number"))

#swap=0;

#print(a)
#print(b)

#swap=a
#a=b
#b=swap

#print("After swapping",a)
#print("After Swaping",b)


#num1=int(input("enter the number"));
#num2=int(input("Enter the number"));

#print("Before Swaping {} {}".format(num1,num2));

#num1=num1+num2;#20+30=50
#num2=num1-num2;#50-30=20
#num1=num1-num2#50-20=30
#print("After Swaping {} {}".format(num1,num2));


num1,num2=[ int(i)  for i in input("enter the number:-")]
print("Before Swaping {} {}".format(num1,num2));
num1=num1+num2;#20+30=50
num2=num1-num2;#50-30=20
num1=num1-num2#50-20=30
print("After Swaping {} {}".format(num1,num2));
