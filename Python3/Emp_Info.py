class Emp_Info():

    '''Ky re Zaatya , Madarchod , Lavdya , Chinnal , Randi ,..........'''


    def __init__(self , ename ,esal , comp , eid):
        self.ename = ename
        self.esal = esal
        self.comp = comp
        self.eid = eid

    def Info(self):
        print("My name is %s " %(self.ename))
        print(" my sal is %f " %(self.esal))
        print("Company name is {} " . format(self.comp))
        print("ID is " , self.eid)
print(Emp_Info.__doc__)
help(Emp_Info)

emp1 = Emp_Info("damodar" , 900000.80 , "Own" ," 1")
emp1.Info()

emp2 = Emp_Info("dams" , 880000.80 , "Own" ," 2")
emp2.Info()
