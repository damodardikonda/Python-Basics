'''num = int( input("Enter the number"))

sum = 0

for i in range(1,num):
    if num % i == 0:
        sum = sum + i ;

if sum == num:
    print(num,"is perfect number ")


n1,n2 = [ int (i) for i in input("Enter 2 numbers"). split()]
fact = 1
for i in range(n1,n2+1):
    fact = fact*i;
    print(fact)


'
c = 1;
n = 1
for i in range(1,5):
    for j in range(1,i+1):
        c=n*n*n
        print(c , end=" ");
        n+=1;
    print()
'''

n1 , n2 , n3 = [int (i) for i in input("Enter 3 number s").split()]

if n1>n2>n3:
    print(n1)
elif n2>n1>n3:
    print(n2)
else:
    print(n3)
