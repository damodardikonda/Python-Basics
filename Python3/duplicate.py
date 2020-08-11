s = input("Enter the String");
n = len(s)
i=0
num=0
while i < n:
    if(s[i] == s[i+1]):
        pass
    else:
        print(s[i],end='')
    i=i+1
