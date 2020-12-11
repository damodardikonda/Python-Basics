class CORONA:

    corona_india = 300000
    def __init__(self):
          self.corona_count = 1,70,000

    def precaution(self):
         print("Corona count is = " , self.corona_count)
         print("Stay Home Stay Safe")

    @classmethod
    def impDaecision(cls):
        print("CM Decision ")
        print(" All Over indians Corona is = " , CORONA.corona_india)

    def all_State():

        all = 300000-170000
        print("All state Excluding Maharashtra is " ,all )


c = CORONA()
c.precaution()
CORONA.impDaecision()
CORONA.all_State()
