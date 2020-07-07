''' Write a Program to Print following Pattern.
        #
      # *
    # * *
  # * * * '''


for i in range(4):
    for j in range(4):
        if(i+j==4):
            print("#",end=" ")
        elif(i+j<=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
