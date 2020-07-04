''' Write a Program to check whether the entered number is Abundant number or not.
{Note: a number can be termed as abundant if the sum of all of its perfect divisors is greater than that number itself,
 e.g. 12: 1+2+3+4+6 = 16 > 12 so 12 is an abundant number.}

 '''

div=0

 num=(int(input("Enter the number")))

for i in range(1,num+1):
    if num%i==0:
        div=div+i

print(div)

if div>num:
    print("{} > {} so {} is an abundant number".format(div,num,div))
