'''Program 1: Write a Program to print an Arithmetic Progression (A.P.) series. Take Starting element, Total count of elements in A.P. & the Common Difference from user.
{Note: an AP (i.e. Arithmetic Progression is such series which has common difference between every consecutive elements, AP of common difference 2 starting from 20 can be: 20, 22, 24, 26 . . .}
Input:
 Starting Element: 1
 Number of Elements: 5
 Common Difference: 6
Output: The AP is: 1 7 13 19 23 '''



start=int(input("Enter the Number:="));
num=int(input("enter the number of Element:="));
diff=int(input("Entter the Difference:="));



i=1;

while i<=num:
    print(start)

    start=start+diff

    print(start, end="")


'''
"""
strt = (int)(input("Starting element : "))
nsize = (int)(input("Number of elements : "))
diff = (int)(input("Common difference : "))
s = 0
print("Output : The AP : ",end=" ")
print(strt,end=" ")
for i in range(1,nsize+1) :
	strt = strt + diff
	print(strt,end=" ")
print()
'''
