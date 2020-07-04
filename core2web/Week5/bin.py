"""
Program 2: Write a Program to Convert entered Octal Number to Binary
Number
Input: Octal Number: 17
Output: Binary Number: 1111
"""
num = (int)(input("Enter any octal number : "))
rem = 0
sum = 0
n=0

while num > 0:
	rem = num % 10
	num = int(num/10)

	if(rem >= 0):
		sum = sum + (rem*pow(8,n))
		n=n+1
print("Equivalent binary number is ",bin(sum),"\n")
