'''

i = 1
sum = 0
while i < 10:
  n = int(input(" Enter the number"))
  if n <= 50:
      sum = sum + n
  else:
      sum = sum + n
      break
  i+=1
print("Sum is " , sum)



name = input("Enter the Name")
surname = input(" Enter the Surname")

print(name + " " + surname)

'''
n = int(input(" Enter the rows"))
for i in range(1 , n+1 ):
    for j in range(n+1 , i ,-1):
        print(end=" ")
    for k in range(1,i+1):
        print(i , end="  ")
    print()
