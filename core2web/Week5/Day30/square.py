''' Write a Program to that accepts an integer value from user
 and prints the Square of each digit.
 Input: 1234
 Output:
   The Square of 1 is 1
    The Square of 2 is 4
    The Square of 3 is 9
    The Square of 4 is 16

 '''
"""
num=int(input("Enter the Number:="))

rem=0;
Square=0;

while num!=0:
    rem=num%10
    Square=rem*rem
    print("Square of "+str(Square));


    num=num/10

    """
    num = (int)(input("Enter the number : "))
    div = rem1 = rem = 0
    while(num > 0) :
    	rem = num % 10
    	num = (int)(num/10)
    	div = div * 10 + rem
    while(div > 0):
    	rem1 = div%10
    	div = (int)(div/10)
    	print("The square of ",rem1," is ",rem1*rem1)
