s = {10,20,30,40}

print(s)
print(id(s))


ss = set()

s.add(20)
s.add(60)
s.add(100)
s.add(99000)
s.add('damodar')
s.add('kh'+'sd')
print(s)


sett={10,20,30}
l=[100,2000,300]
x={3000,4000,5000}
y=(988,555,674)
sett.update(l,x,y)
sett.update('kh' + 'sdf')
print(sett)


s.pop()
s.pop()
s.pop()
print(s)

s.remove(20)
print(s)

sett.discard(2000)
sett.discard(4000)
print(sett)
