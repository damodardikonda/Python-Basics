''' Write a Program to print table in reverse order.
Input : 2
Output :
2 X 10 = 20
2 X 9 = 18
 2 X 8 = 16
. '''


#num=int(input("Enter the number"));
#for i in range(10,0,-1):
#    n1=num*i;
#    print(n1)


try:
    num=int(input("Enter the number"));
except ValueError as ve:
    print("It is not a Number");
    pass

if(num<0):
    print("Negetive Number")
else:
    i=10;
    while i<1:
        table=num*i
        print("Table is",table)
        i=i-1
