"""

Program 5: Write a Program to check whether the number is divisible by 5 &
11 or not.
Input: 55
Output: 55 is divisible by 5 & 11.

"""

a=57;

if a%5==0 and a%11==0:

    print(str(a)+"{} is divided by 5 and 11"); #unsupported operand type(s) for +: 'int' and 'str'......
    # he tell that string and int is not compatible with each other
else:
    print("{} is divided by a5 and 11".format(a));
