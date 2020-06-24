a=int(input("enter the number"));

if a<0:
    print("number is less than Zero");

else:
    for i in range(1,a*a+1):
        if i%a==0:
            print("*");
        else:
            print("*",end='')
