'''

 * * *
  * * *
   * * *



for i in range(1,4):
    for j in range(0,i):
        print(end = " ")
    for k in range(1,2):
        print("* * * " , end=" ")
    print()


for i in range(1,4):
    for j in range(4,i):
        print(end=" ")
    for  k  in range(1,2):
        print("* * * " , end=" ")
    print()


y = int(input("Enter the Number "))

if y % 4 == 0:
    print("it is leap year")
else:
    print("It is not a Leap Year")


x,y,z = [int(i) for i in input("Enter 3 number ").split()]

if x>y>z:
    print(x," is greater")
elif y>x>z:
    print(y," is greater")
else:
    print(z ," is greater")


'''

import sys
a  = sys.argv[1]
b = sys.argv[2]
add = int(a)+int(b)

print(add)
