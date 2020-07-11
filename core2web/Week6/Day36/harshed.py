num=int(input("Enter the number"));
temp=num
rem=0;
a=0;

while num!=0:
    rem=num%10;
    a=a+num

    num=num//10;

print(a)

print(f'{temp} is an hashed number..');
print(f'{a} is perfect number');
