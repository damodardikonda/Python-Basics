'''
Write a Program to Print following Pattern.
 C O R E
   O R E
     R E
       E
       '''
for i in range(1,5):
	for j in range(1,5):
		if(i-j)<=0 and j==1 :
			print("C",end=" ")
		elif(i-j)<=0 and j==2 :
			print("O",end=" ")
		elif(i-j)<=0 and j==3 :
			print("R",end=" ")
		elif(i-j)<=0 and j==4 :
			print("E",end=" ")
		else :
			print(" ",end=" ")
	print()
