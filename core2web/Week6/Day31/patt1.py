'''

Write a Program to Print following Pattern.

   0 1 4 9 16
    1 6 12 20
      8 15 24
        18 28
           32

           '''
a=2
for i in range(1,6):
   for j in range(1,6):
       if (j<i):
           print(\t,end="")
       else:
           print(j*2,end="")
           print()
       a=a+1
