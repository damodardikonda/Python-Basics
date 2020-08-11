lb=int(input("Enter tthe Number"));
ub=int(input("ENter the upper bound"));



for i in range(lb,ub+1):
    num=i;
    s=0;
    while n!=0:
        s+=num%10
        num=int(num/10)
    if(i%s==0):
        print(i,end='')
