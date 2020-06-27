try:
     n=int(input("enter the number"));
except ValueError as ve:
     print("Wrong Value");
     pass

if(n%2==0):
   print("Even number")
else:
   print("odd Number");
