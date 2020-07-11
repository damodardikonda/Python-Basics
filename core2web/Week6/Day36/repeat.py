num=int(input("Enter the number"));

repeat=(int)input("Enter the Number");
rem=count=0;
while num>0:
    rem=num%10;
    temp=rem
    num=num//10;
    if temp==num:
        count+=1

print(f'{repeat} is repeatd for {temp} times')
