'''

Write a Program to print series of Even numbers ranging between two numbers entered by user.
Input:
Min of Series : 4
 Max of Series: 60
Output: Series Of Even Numbers Ranging between 4 & 60 is:
4, 6, 8, . . ., 60
'''

#min=int(input("Enter the Minimum Number:="));
#max=int(input("Enter the Maximum Number:="));

#for i in range(min,max):

 #  if i%2==0:
#       print(i, end=" ")


#min,max=[int(i) for i in input("Enter the minimum and maximum number:=").split("")]
#for i in range(min,max):

 #  if i%2==0:
#       print(i, end=" ")


try:
      min=int(input("Enter the Minimum Number:="));
      max=int(input("Enter the Maximum Number:="));
except valueError as ve:
      print("please Enter number")
      pass

for i in range(min,max):

   if i%2==0:
       print(i, end=" ")
