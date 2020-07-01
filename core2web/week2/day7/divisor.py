'''Write a Program to that accepts two integers from user and calculates
the Quotient & Reminder from their division
 Input: 10 5
 Output:   Quotient: 2
            Reminder: 0 '''



n1,n2=[int(i) for i in input("Enter The Number").split()]

Quotient=n1/n2
print("Quotient is",Quotient)

Remainder=n1%n2
print("Remainder is", Remainder)
