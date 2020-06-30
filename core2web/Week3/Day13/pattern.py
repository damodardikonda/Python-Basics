'''
Write a Program to Print following Pattern.
1
4 9
16 25 36
49 64 81 100 '''

#k=1
#for i in range(1,k+1):
#    for j in range(1,i):
#        square=i*i
#        print(square)
#    print()



rows = int(input("Enter number of rows\n"))
num = 1

for x in range(rows):
    for y in range(x+1):
        print(num*num,end="\t")
        num = num + 1
    print()
