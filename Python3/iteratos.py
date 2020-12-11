list = [1,2,3,4,5,56,67,78]

i_list = iter(list)

#print(i_list.__next__())
#print(next(i_list))

#print(i_list.__getitem__(1))

for i in i_list:



      print(i)


'''
tup = (1,4,23,67,45,)

i_tup = iter(tup)

print( next(i_tup))
print(next(i_tup))

for i in i_tup:
    try:

        p = next(i_tup)
        print(p)

    except StopIteration:
        break


'''

s = { 1,2,3,4,5,6,7,8,9}

i_s = s.__iter__();

print(next(i_s))


for i in i_s:
   print(i)
