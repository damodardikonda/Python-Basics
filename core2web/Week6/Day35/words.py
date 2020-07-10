'''
 Write a Program that takes a number as input from user and prints it into words.
  Input: 1234
  Output: One Two Three Four

  '''


n=int(input("enter the Number:="));
num=0;
for i in range(0,num):
    num=n%10;

    if num==1:
       print("one",end="");
    elif num==2:
        print("Two",end="");
    elif num==3:
        print("Three",end="");
    elif num==4:
        print("Four",end="");
    elif num==5:
        print("Five",end="");
    elif num==6:
        print("Six",end="");
    elif num==7:
        print("Seven",end="");
    elif num==8:
        print("Eight",end="");
    elif num==9:
        print("Nine",end="");
    else num==10:
        print("Ten",end="");

    num=num//10;
