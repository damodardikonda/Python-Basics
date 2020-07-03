''' Write a Program that prints following pattern.
       4
     3 4
   2 3 4
 1 2 3 4
'''



for itr in range(0,4):

    for jtr in range(0,4):
        print(" ",end="\t")if jtr<3-itr else print(jtr+1,end="\t")
    print("")



'''for i in range(0,4):
       for j in range(0,4):
           print(" ",end="\t") if j<3-i else(j+1,end="\t")
       print("")


       '''       
