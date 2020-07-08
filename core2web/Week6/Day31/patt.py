'''
Write a Program to Print following Pattern.
 5 4 3 2 1
   4 3 2 1
     3 2 1
       2 1
         1
 '''
 '''
size = (int)(input("Enter the size : "))
for i in range(1,size+1) :
	temp = size
	for j in range(1,size+1) :
		if((j-i)>=0):
			print(temp,end=" ")
		else :
			print(" ",end=" ")
		temp = temp - 1
	print()
'''

size = (int)(input("Enter the size : "))
for i in range(1,size+1):
    temp=size
    for  j in range(1,size+1):]
        if((j-i)>=0):
           print(temp,end="")
        else:
           print("",end=" ")

         temp=temp-1
    print()
