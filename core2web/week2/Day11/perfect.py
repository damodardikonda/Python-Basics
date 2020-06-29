'''  Write a Program that accepts an integer from user and prints all of its perfect divisors.
Input: 24
Output: Perfect Divisors of 24 are: 2 3 4 6 8 12

 '''
num=int(input("Enter the Number:"))

for i in range(2,num-1):
    if num%i==0:
        print("{} is divisible by{}".format(num,i));
