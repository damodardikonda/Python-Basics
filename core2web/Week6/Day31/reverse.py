''' Write a Program to display a number in reverse order.
Input: 123456
Output: 654321
  '''
num=int(input("Enter the number"));


for i in range(len(num)-1,-1,-1):
    print(num[i],end="")
print()
