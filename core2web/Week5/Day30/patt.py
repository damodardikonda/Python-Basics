'''
Write a Program to Print following Pattern.
       100
     81 64
  49 36 25
 16 9 4 1
'''
num=10
for i in range(4):
    for j in range(4):
        if(i+j)>=4:
            print(num*num,end=" ")
            i=i-1;
        elif(j<=i):
            print(end="")

    print()
