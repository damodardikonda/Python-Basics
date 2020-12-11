for i in range(10,0,-1):
     print(2*i);
'''
n =int( input(" Enter the number"))
n1 = n-2
print(n1)
print(n++2)
'''
n=2
for i in range(1,5):
    for j in range(1,i+1):
        print(n+j , end=" ")
    n = n- 1
    print()

d , y , m = [int(i) for i in input(" Enter date year month").split()]

if(m == 1 or m==3 or m == 6 or m==8 or m==10 or m== 12) and (d <=31):
    print("valid")
