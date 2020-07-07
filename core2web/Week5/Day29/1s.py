''' Write a Program that takes a number as input from user and
prints the counts the occurrence of 1’s from it.
Input: 1211234
 Output:  The number 1211234 Contains 3 One’s
 '''


num=int(input("Enter the number"));

rem=0;
count=0;



if num!=0:
    rem=num%10
    if rem==1:
        count=count+1
    num=num/10;



print(f"the number {num} contains {count}  one's")
