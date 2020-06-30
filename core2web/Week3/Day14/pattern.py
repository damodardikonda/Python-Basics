'''Write a Program to Print following Pattern.
 1
 8 27
 64 125 216
 343 512 729 1000 '''

k=int(input("Enter the rows"));
for itr in range(1,k+1):
    for inner in range(itr):
         print(itr*itr*itr, end=" ")
         itr=itr+1

    print()
