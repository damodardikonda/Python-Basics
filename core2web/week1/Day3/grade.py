"""
Program 5: Write a Program to take marks of five subjects Physics, Chemistry, Biology,
 Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
"""

Physics=int(input("enter the Physics marks"));
Chemistry=int(input("enter the Chemistry marks"));
Biology=int(input("enter the vBiology marks"));
Mathematics=int(input("enter the Mathematics marks"));
Computer=int(input("enter the Computer marks"));


total=500;

total_marks=Physics+Chemistry+Biology+Mathematics+Computer;

Percentage=float(total_marks/total*100)

if Percentage>=90:
    print("Grade A")

elif Percentage>=80 and Percentage<=90:
    print("Grade B")

elif Percentage>=70 and Percentage<=80:
    print("Grade C")
elif Percentage>=60 and Percentage<=70:
    print("Grade D")
elif Percentage>=50 and Percentage<=60:
        print("Grade E")
elif Percentage>=40 and Percentage<=50:
    print("Grade F")
