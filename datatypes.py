import re
#int
import random as ran;

a=123+45
print(a)

b=2*3.5
print(b)


print(ran.random())

num=2**299
print(len(str(num)))

#string
s='abcd'
print(s[0])
print(s[3])
print(s[-2])
print(s[-1])
print([len(s)-1])
print(len(s*6))

#strings are immutable s[0]='z' is gives an error

s='z'+s[1:]
print(s)
print(s.find('bc'))
print(s.replace('bc','defg'))
print(s)#op will zbcd
print(s.isalpha())
print(s.isdigit())

print('{0},egg,hicken,{1}'.format('spam','SPAM'))
c='a\nb\tc'
print(len(c))

print(ord('\n'))

match=re.match('hello[\t]*(.*)world','hello        python world')
print(match.group(1))
print(match.group())





#list

l=[1,2,3.5,'abd']
print(len(l))
print(l[0])
print(l[:-2])
new=l+[76,45,82]
print(new)
print("Inserting at location 2")
print(new.insert(2,8999999))
print('adding each element as a variable')
n=[90,36,69]
print(new.extend(n))
new.append('x1')
print(new)
print("removing an elementssssss")
print(new.remove('x1'))

print("finding index")
sss=new.index(90)
print(sss)
print("reverse a list")
print(new.reverse())
print(new.pop())

print(new.pop(2))
print(new.insert(34,2))
print(new)

print(new.remove('abd'))
print(new)
print(new.sort())
print(new)
print('sort thr listt')
s=sorted(new)
print(s)
print(new.reverse())
print(new)

mullist=[[1,2,3,5],[4,5,6,8],[7,8,9],[5,3,8]]
print(mullist[2][2])#prints 9

col=[r[1] for r in mullist]
print(col)

col2=[row[1]+1 for row in mullist]
print(col2)

col3=[row[1] for row in mullist if row[1]%2==0]
print(col3)

dia=[mullist[i][j] for i in[0,1,2] for j in[1,2,0]]
print(dia)

l=[c*2 for c in 'spam' ]
print(l)
sr=[sum(row) for row in mullist]
#print(next(sr))#6
print(sr)#6,15,25

dd=[[8,4,9],[3,9,5]]
sc=[sum(col) for col in dd]
print(sc)
