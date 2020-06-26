"""
Program 4: Write a Program to Print following Pattern
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""
i = 1;
for x in range(4):
	for y in range(4):
		print(i," ",end=" ")
		i=i+1;
	print()
