''' Write a Program that computes sum of all possible divisors of an entered number.
 Input: 24
  Output: The of all possible divisors of 24 is : 39
'''

num=int(input("Enter the Number"));

for i in range(1,num-1):
if num%i==0:
    divisor=divisor+i

print("The all Possible divisor is  ",divisor)


try:
    num=int(input("Enter the Number"));

except Exception as e:
    print("Enter Positive Number");
    pass


for i in range(1,num-1):
if num%i==0:
    divisor=divisor+i

print("The all Possible divisor is  ",divisor)
