for i in range(100,1,-1):
    if  i % 2 == 1:
        print(i , end=" ")

print()
print()

for i in range(100,1,-2):
    print(i , end= " ")

print()
print()
for i in range(1,5, 1):
    for j in range(4,i-1,-1):
        if j % 2 == 0:
            print("+" , end=" ")
        else:
            print("=" , end=" ")
    print();

print()
n1 , n2 = [int(i) for i in input(" Enter the number").split()]
b = 0
max = 0
if n1 > n2:
    b = n1
else :
   b = n2

 for i in range(1, b, 1):
     if n1 % i == 0 and n2 % i == 0:
         max = i

print(max)
