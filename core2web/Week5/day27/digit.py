'''

: Write a Program that takes a number as input from user and
prints the counts the occurrence of odd digits from it
Input: 123458
 Output: The number 123458 has 3 Odd digits.
 '''

num=int(input("enter the number"))

rem=0
count=0

while num!=0:
    rem=num%10

    if rem%2!=0:
        count=count+1


    num=num/10

print(num)
