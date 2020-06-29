: Write a Program to Print following Pattern.
a
A A
a  a a
A A A A
a a a a a

for i in range(5):
    for j in range(1,i+1):
        if j%2==1:
            print("a" end="")
        else:
            print("A")
        print("")
