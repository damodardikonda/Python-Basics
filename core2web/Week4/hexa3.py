''' Write a Program to convert entered Binary Number to Hexadecimal Number.
Input: Binary Number: 1011
Output: Hexadecimal Number: B
 '''


n1,n2,n3,n4=[int(i) for i in input("Enter the 4 digit number").split()];

a=0;
b=0;
c=0;
Binary=0
if n4==1:
    a=1
else:
    a=0

if n3==1:
    b=2
else:
    b=0


if n2==1:
    c=4
else:
    c=0

hexa=a+b+c;
print(hexa)

if Binary==1011:
    print("A");
elif Binary==1100:
    print("B");
elif Binary==1101:
    print("C");
elif Binary==1110:
    print("D");
elif Binary==1111:
    print("E")
