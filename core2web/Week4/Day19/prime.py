''' Write a Program that checks whether the entered number is a Prime Number or not.
{Note: A Prime Number is that number which is only divisible by 1 & that number only.}
Input: 5
Output: 5 is Prime Number. '''


num=int(input("enter the number"));

if num%1==0 and num%num==0:
     print("prime number")
else:
    print("Not a prime number");


try:
     num=int(input("enter the number"));
except valueError as ve:
    print("Enter the Number");
    pass


if num%1==0 and num%num==0:
     print("prime number")
else:
    print("Not a prime number");
