''' Write a Program to Print following Pattern.
 3
 2 3
 1 2 3
 0 1 2 3 '''

for i in range(4):
    for j in range(i + 1):
        print(3 - i + j, end = " ")
    print()
