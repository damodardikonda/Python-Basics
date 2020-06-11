def gener(mynum):
    res=[]
    for i in mynum:
        res.append(i*i)
    return res

mynum=gener([1,2,3,4,5])


print(mynum)



print('yield is used for generator')

def generators(n):
    r=[]
    for i in n:
        yield(i*i)
    return r

gen= generators([1,2,3,4,5])


for nu in gen:
    print(nu)

number=(x*x for x in [1,2,3,4,5])#() it is a sign of generator

print(list(number))
