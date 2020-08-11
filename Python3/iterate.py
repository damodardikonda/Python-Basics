
#break statements
for i in range(10):
    if i==5:
        print(i)
        break


#Continue

list=[10,20,30,600,40,78,520]

for i in list:
    if i >=500:
        print("SOrry you cant buy it ....You have to required insurance");
        continue
    print("Item=",i);

l=[10,5,2,0,50,20,0]
div=0;
for i in l:
    if i == 0:
        print("Divided By Zero");
        continue
    div=100/i
    print("division is = ",div)
