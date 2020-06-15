import re
a=input("Enter the file name")
z=list()
for x in a:
    y=re.findall('/S[a-z]/S',x)
    z=y.split()
print(list)
