'''a1 , a2 = [int(i) for i in input("Enter 2 numbres").split()]

for i in range(a1,a2,2):
    print(i , end=" ")


if a1 > a2 :
    print("Minimum is " , a2)
else:
    print("Minimum is " , a1)


dist , time = [int(i) for i in input("Enter 2 number").split()]

velocity = dist/time
print(int(velocity))

'''
a= 1;

for i in range(1,5):
    for j in range(1,i+1):
        print(a*a ,end=" ")
        a+=1;

    print()
