'''Write a Program that calculates the Greatest Common Divisor of two entered numbers.
 Input: 25 15 Output: The GCD of 25 & 15 is 5.
 '''

n1,n2=[int(i) for i in input("Enter the Number:").split()]

i=2
while i<n1 or i<n2:
    if n1%i==0 and n2%i==0:
        print(i)
        i=i+1
