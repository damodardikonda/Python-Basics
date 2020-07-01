'''4: Write a Program to Print following Pattern.
 7
 6 5
 5 4 3
 4 3 2 1 '''

n=int(input("Enter the Number"));
k = n * 2 - 1
for i in range(1,n+1):
	for j in range(1,i + 1):
		print(k, end = "\t")
		k = k - 1

	k = n * 2 - 1 - i
	print()
