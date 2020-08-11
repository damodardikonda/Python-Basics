num1=300
num2=600
temp =0
for i in range(num,num2+1):
    temp=i;
    if(temp % i==0 and temp % 1==0):
        print(temp,end='')
