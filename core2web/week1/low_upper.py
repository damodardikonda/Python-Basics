ch=input("enter the character");


try:

       if(ord(ch)>=65 and ord(ch)<=90):
             print("{} is an UpperCase letter".format(ch));
       elif ord(ch)>=97 and ord(ch)<=122 :
             print("{} is an lowecse letter".format(ch));
       else:
             print("number");

except TypeError as te:
   print("no number type")
