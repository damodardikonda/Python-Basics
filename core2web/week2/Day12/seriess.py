'''Write a Program to print series of odd numbers ranging between two numbers entered by user.
Input:
Min of Series : 4
  Max of Series: 60
Output: Series Of Odd Numbers Ranging between 4 & 60 is:
 5, 7, 9, . . ., 59
 '''

odd=[]
num1=int(input("enter the starting Number:"))

num2=int(input("enter the ending Number:"))

for i in range(num1,num2):

        if i%2==1:
           print(i)
