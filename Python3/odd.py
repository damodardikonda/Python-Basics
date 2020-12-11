a,b = [int(i) for i in input(" Enter 2 numbers  ").split() ]

for i in range(a , b):
    if i % 2 == 1:
        print(i , end=" ")
