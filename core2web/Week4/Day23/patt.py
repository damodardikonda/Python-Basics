''' Write a Program to Print following Pattern.
      D
    C D
  B C D
A B C D '''


for i in range(4):
    for j in range(4):
        if(j<n-i):
            print(end="\t")
        else:
            print(chr(68),end="\t")
    print()
