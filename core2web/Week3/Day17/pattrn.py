'''Write a Program to Print following Pattern.
A A A A A
B B B B
C C C
D D
E'''

n = int(input("Enter Size "))

for outer in range(1,n+1):
    for inner in range(1,n-outer+2):
        print(chr(64+outer), end ="\t")
    print()
