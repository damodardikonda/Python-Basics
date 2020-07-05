'''Write a Program that takes a number as input from user and
 prints the digit count from that number.
  Input: 123458 Output: The number 123458 has 6 digits.


n = int(input("Enter Number : "))
cnt=0
while(n != 0):
	n = n // 10
	cnt+=1

print("Count : ", cnt)
'''


p=list()

p=input("enter the number")

print(len(p))
