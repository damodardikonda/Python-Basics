def calc(x,y):
    add = x+y
    sub = x-y
    mul = x*y

    return add , sub , mul

t =  calc(x=100,y = 50)
for c in t:
    print(c)


x =  calc(y=50,x = 100)
for c in x:
    print(c)


l =  calc(100,y = 50)
for c in l:
    print(c)

'''
a =  calc(x=100, 50)  #Not Allowed
for c in a:
    print(c)
'''
