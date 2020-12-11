'''s1={10,20,30,40,50}
s2={10,20,60,70}

print(s1.union(s2))
print(s1|s2)

print(s1.intersection(s2))
print(s1&s2)

print(s1-s2)
print(s1.difference(s2))

print(s1^s2)
print(s1.symmetric_difference(s2))


#membership operator

print(10 in s1)
print(90 in s1)

print(100 not in s1 )
'''
#Set Comprehension

set = {x*x for x in range(5,10)}
print(set)
