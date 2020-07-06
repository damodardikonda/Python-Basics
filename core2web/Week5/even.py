''' Write a Program that takes a number as input from user
 and prints the counts the occurrence of even digits from
 it Input: 123458 Output: The number 123458 has 3 Even digits.
 '''
num=int(input("entee the number"));

rem=0;
count=0;

while num!=0:
    rem=num%10;

    if num%2==0:
        count=count+1
        num = num/10

print(count)
