class ITCOMP:

       def __init__(self):
             self.proj = self.CAPGEMINI(200)
             self.p =self.TCS(240)


       def dispProject(self):
               print("outer class")
               print("Number of Capgemini Projects Ar = " , self.proj.dispProject())
               print("Number of TCS Projects Are = " , self.p.dispProject())


       @classmethod

       def clsMethod(cls, tp):
              cls.employee =cls. CAPGEMINI.dispEmp(100)
              CAPGEMINI.dispEmp();






       class CAPGEMINI:

            no_of_emp = 200000

            def __init__(self , project):
                self.no_of_project = project

            def dispProject(self):
                 print("Number of Projects Are = " , self.no_of_project)

            @classmethod
            def dispEmp(cls,tp):
                self.tp_project = tp
                print("Numbers of Employees are = " , cls.no_of_emp)

       class TCS:

             no_of_emp = 300000

             def __init__(self,project):
                  self.no_of_project = project

             def dispProject(self):
                   print("Number of Projects are = " ,self.no_of_projetc)

             @classmethod
             def dispEmp(cls):

                   print("Numers of employees are = " , TCS.no_of_emp)



t = ITCOMP()
c = t.CAPGEMINI()
c.dispProject()
CAPGEMINI.dispEmp()


tcs = t.TCS()
tcs.dispProject()
TCS.dispEmp()
