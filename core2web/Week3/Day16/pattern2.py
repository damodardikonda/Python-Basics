'''
7
 7 6
 6 5 4
 4 3 2 1 '''


for i in range(4):
    for inner in range(i+1):
        print(7-inner+i, end=" ")
    print()
