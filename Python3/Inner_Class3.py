class Person:

    def __init__(self):
        self.name = "Damodar"
        self.Sur_Name = "Dikonda"
        self.dob = self.DOB()

    def Display(self):
        print("Name is " , self.name);
        print(" Sur_Name is " , self.Sur_Name)
        self.dob.dispDob();


    class DOB:

       def __init__(self):
          self.day = 3
          self.month = 4
          self.year = 2000

       def dispDob(self):
           print("date is = {}/{}/{} "  .format(self.day , self.month ,self.year));


p = Person()
p.Display()
