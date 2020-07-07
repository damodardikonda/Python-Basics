
'''
 Write a Program that takes a number as input from user
  and prints the counts the occurrence of Odd Digits &
  Even Digits from it
  Input: 123458
  Output:  The number 123458 Contains 3 Odd Digits & 3 Even Digits.

 '''


num=int(input("Enter the Number:="))

rem=0;
i=0;
j=0;

 while num!=0:
     rem=rem%10

     if rem%2==0:
         i=i+1
     else:
         j=j+1;

         
     num=num/10
