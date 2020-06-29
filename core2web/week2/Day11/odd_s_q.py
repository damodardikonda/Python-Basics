'''
: Write a Program to print Cubes and Squares of all Odd numbers ranges between given input number.
 Input:  10
 Output:
   Cube of 1 : 1 and Square of 1 :1
     Cube of 3 : 27 and Square of 3 :9
   .
   .
     Cube of 9 : 729 and Square of 9 : 81
 '''


#num=int(input("Enter the starting Number :"));
#num1=int(input("Enter the ending Number :"));

#for i in range(num,num1):
#    if i%2==1:
#        square=i*i;
#        print(i,"-->",square)
#        cube=i*i*i;
#        print(i,"-->",cube)


#num[0],num[1]=(input("Enter the number:-")).split();
#for i in range(num,num1):
#    if i%2==1:
#        square=i*i;
#        print(i,"-->",square)
#        cube=i*i*i;
#        print(i,"-->",cube)


try:
      num=int(input("Enter the starting Number :"));
      num1=int(input("Enter the ending Number :"));

except valueError as ve:
    print("enter the number not string")
    pass

for i in range(num,num1):
    if i%2==1:
        square=i*i;
        print(i,"-->",square)
        cube=i*i*i;
        print(i,"-->",cube)
