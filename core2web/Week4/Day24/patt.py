'''Write a Program to Print following Pattern.
      =
    = 1
  = 1 2
= 3 4 8
 '''

for i in range(4):
    for j in range(4):
        if(j<4-i):
            print("=" end="\t")
        else:
            a=j
            a=a-1
            print(j+a)
    print()
