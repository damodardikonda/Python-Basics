ch=input("enter the letter:=");

if ch>="A" and ch<="Z" or ch>='a' and ch<='z':
    print(ch,"is an letter");
elif  ord(ch)>=48 and ord(ch)<=57:#ord is used for find out ascii value
    print(ch,"it is an number");
elif ord(ch)>=33 and ord(ch)<=47 or ord(ch)>=58 and ord(ch)<=64:
    print("Special Character");
