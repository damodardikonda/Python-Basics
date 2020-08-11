'''n=eval(input("Enter the Number"));

sum=0;
i=0;
while i<=n:

    sum=sum+i;

print(sum);



name=''
password=' '

while name!='damodar' and password != 'dams123':// while (name!='durga') & (pass != 'dams123')
    name=input("Enter name again");
    password = input("Eneter the password")

print("Welcome damodar");
''

#Nested for Loops

for i in range(4):
    for j in range(4):
        print('i={} and j={} '.format(i,j))
''

for i in range(1,5):
    for j in range(1,i+1):
        print("*", end='\t')

    print()
''
n=int(input("Enter the Number"));
for i in range(n):
    print('*'*n , end='')
    print();

''
n= int(input("Enter the Number"))
for i in range(1 , n+1):
    print("*"*i,end='')
    print()

''

x=10
y=20
z=30

del x,y,z
print(x)
print(y)
print(z)
''
x=10
y=10
z=30

del x
print(y)


'''

s= 'My name is "Damodar" '
print(s)

d="This is \"Double quotes\" Symbols"
print(d)
