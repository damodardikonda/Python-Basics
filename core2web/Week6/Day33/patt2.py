'''
Write a Program to Print following Pattern.

  0 1  10  11
   10  11 100
       100 101
           110
           '''

for i in range(1,5) :
	for j  in range(1,5) :
		if ((i-j)<=0 and (i+j) == 2):
			print("0",end="\t")
		elif ((i-j)<=0 and (i+j) == 3):
			print("1",end="\t")
		elif ((i-j)<=0 and (i+j) == 4):
			print("10",end="\t")
		elif ((i-j)<=0 and (i+j) == 5):
			print("11",end="\t")
		elif ((i-j)<=0 and (i+j) == 6):
			print("100",end="\t")
		elif ((i-j)<=0 and (i+j) == 7):
			print("101",end="\t")
		elif ((i-j)<=0 and (i+j) == 8):
			print("110",end="\t")
		else :
			print(" ",end="\t")
	print()
