'''Write a Program to print AP in reverse order take last Element
& Common Difference from user. {Note: Use While Loop}
Input:   Last Element In AP: 40  Common Difference: 8

Output: 40 32 24 16 8 '''


num=int(input("Enter the Number:="));
diff=int(input("Enter the Difference"));
while num!=0:
    num=num-diff
    print(num,end="")
