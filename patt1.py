''' Write a Program to Print following Pattern.
      4
    3 4
  2 3 4
1 2 3 4 '''

for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<n-i):
            print(end="\t")
        else:
            print(n)
            n-=1
    print()
