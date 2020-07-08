''': Write a Program that takes a number as input from
user and prints the factorials of each digit.
Input: 141
Output:  The Factorial of 1 is 1.
The Factorial of 4 is 24.
 The Factorial of 1 is 1.
'''
num=int(input("Enter The Number:="));
div=0;
rem=0
while(num>0):
    rem=num%10;
    num=num/10
    div=(int)(num*10+rem);
while (div>0):
    fact=1
    rem=div%10
    div=(int)(div/10+rem)
    for i in range(1,rem+1):
        fact=fact*i;
    print("factorial of", i," is"," fact")





"""
num = (int)(input("Enter the number : "))
rem = div = rem1 = 0

while(num > 0) :
    rem = num%10
    num = (int)(num/10)
    div = div * 10 + rem


while(div > 0) :
	fact = 1
	rem = div % 10
	div = (int)(div/10)
	for i in range(1,rem+1) :
		fact = fact * i
	print("The factorial of",i," is ",fact)
"""
