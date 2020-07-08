''': Write a Program to print sum of following series. Take the limiting factor from user and print sum up to that element.
Series: 1, 11, 111, 1111, 11111, 111111, 111111 . . .
Input: 5
Output: The Sum is: 12345
 '''

num=(int)(input("Enter the number:="));

for i in range(1,num+1):
    print("1"*i,end="")

print()


for i in range(1,num+1):
    print(0+i,end="")
print()
