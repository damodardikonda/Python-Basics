''' Write a Program to Print following Pattern.
0
1 1
0 0 0
1 1 1 1
0 0 0 0 0 '''



for itr in range(5):
    for outr in range(0,itr+1):
     if itr%2==0:
         print("0",end=" ")
     else: print("1",end = " ")
    print(" ")
