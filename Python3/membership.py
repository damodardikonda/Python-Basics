'''s='DamodaR'
print('r' in s)
print('o' in s)

main_s =input("Enter the Main Stream");
sub_s = input("Enter the Sub Stream");

if sub_s in main_s:
    print(sub_s , "is found in main stream");
else:
    print(sub_s , "is not found in main stream");
''
s1 = input("Enter the String s1");
s2 = input(" Enter the String s2");

if s1 == s2:
    print("Both String are Equal");
elif s1 > s2:
    print("S1 is greater than s2");
else:
    print("s2 is greater than s1");
'''

l1  = ["A","B","C"]
l2 =["A","B","C"]

print(l1 == l2)
print(l1 is l2)
