class Emp_Info():

    '''Ky re Zaatya , Madarchod , Lavdya , Chinnal , Randi ,..........'''


    def __init__(s , ename ,esal , comp , eid):
        s.e1 = ename
        s.e2 = int(esal)
        s.e3 = comp
        s.e4 = eid

    def Info(x):
        aa = 2
        print(aa)
        print("My name is %s " %(x.e1))
        print(" my sal is %f " %(x.e2))
        print("Company name is {} " . format(x.e3))
        print("ID is " , x.e4)
print(Emp_Info.__doc__)
help(Emp_Info)

emp1 = Emp_Info("damodar" , 900000.80 , "Own" ," 1")
emp1.Info()

emp2 = Emp_Info("dams" , 880000.80 , "Own" ," 2")
emp2.Info()
