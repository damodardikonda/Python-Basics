''' Write a Program that takes a number as input from user
 and prints only those digits from that number,
  which are perfect divisors of the actual number.
 Input: 124
Output: The Perfect Divisor Digits from the Number 124 are 1 2 4
 '''


num=int(input("Enter the numer"))
num1=num
rem=0
print("The Perfect Divisor Digits From the Number",num,"are",)

while num!=0:
    rem=num%10
    num=num//10
    if(num1 % i == 0 and rem == i) :
        print(i,end=" ")
rem = 0
print()



    '''

num = (int)(input("Enter the number : "))
num1 = num
rem = 0
print("The perfect divisor of ",num," are ",end=" ")
while num > 0 :
	rem = num % 10
	num = num // 10# provide int value not decimal
	for i in range(1,rem+1) :
		if(num1 % i == 0 and rem == i) :
			print(i,end=" ")
	rem = 0
print()
'''
