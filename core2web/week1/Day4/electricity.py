'''Write a program that takes electricity unit charges as input
 and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit. '''

unit=float(input("Enter the Units"));

if unit<=50:
    rs=unit*0.50;
    print( "Rs. {}/unit".format())

elif  unit<=100:
    rs=unit*0.75;
    print( "Rs. {}/unit".format())

elif  unit<=200:
    rs=unit*1.2-0;
    print( "Rs. {}/unit".format())

elif  unit<=250:
    rs=unit*1.50;
    print( "Rs. {}/unit".format())
else:
    rs=unit*1.75;
    print( "Rs. {}/unit".format())
