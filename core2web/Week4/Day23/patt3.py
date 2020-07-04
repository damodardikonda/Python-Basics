''': Write a Program that prints following pattern.
  = 2 3 4
  1 = 3 4
  1 2 = 4
  1 2 3 =
'''

try:
    n=int(input("Enter the Number"));
except ValueError as ve:
    print("Enter Positive Number");
    pass


for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n:
            print("=")
        else:
            print(j ,end="\t")
    print()
    
