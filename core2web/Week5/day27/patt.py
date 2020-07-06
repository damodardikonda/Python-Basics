''' Write a Program to Print following Pattern.
         9
      9 16
   9 16 25
 9 16 25 36
 '''
a=7

num=int(input("enter the number"));
inc=0
for i in range(1,num+1):
    for j in (1,num+1):
        if(j<num-i):
            print(end="\t")
        else:
            print(9,9+a+inc)
            inc=inc+2
    print()
