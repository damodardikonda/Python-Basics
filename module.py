
print('importing')
test='test string'

def to_Find(to_search,target):

   for i,value in enumerate(to_search):
       if value==target:
         return 1
   return -1
