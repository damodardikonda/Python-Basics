
'''
num = (int)(input("Enter the number : "))
num1 = num
rem = div = 0
while num > 0:
	rem = num % 10
	num = num // 10
	div = div * 10 + rem
if div == num1 :
	print(str(num1)+" is a Palindrome Number.")
else :
	print(str(num1)+" is not a Palindrome Number.")
'''


num=int(input("enter the number"))
num1=num
rem=div=0;
while num>0:
	rem=num%10
	num=num//10
	div=div*10+rem

if div==num1:
	print(str(num1)+"is an palindrom number")
else:
	print(str(num1)+" is not a palindrom number")
