#def calc(name = " damodar " , msg):pass


def calc(name,msg="King"):
    print(msg)
    print(name)

calc("damodar" , "Fan of thor")



def addd(* n):
    sum=0
    for x in n:
        sum = sum + x
    print(sum)
#addd()
#addd(10,20)
addd(1,2,3,4)
#addd(1,2,3,4,5,6,67,8,9,2,2,3,4,56,67,7,88,856,"Damodar" ,"Dikonda" ,89.46,)
