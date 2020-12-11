class Flat:

    tv = " Samsung"
    sopha = 3

    def __init__(self,no_of_mob,dad_mob,bro_mob , my_mob):
        self.no_of_mob = no_of_mob
        self.dad_mob = dad_mob
        self.bro_mob = bro_mob
        self.my_mob = my_mob


    @classmethod
    def dispStatic(cls , bed ):
        cls.bed = bed

        print(" TV name is = " ,cls.tv )
        print("Sopha count is =  " , cls.sopha )
        print("Bed count is =  " ,cls. bed )
        print("NO of CupBoardsa = " , cls.cupboard)

    def Display(self):
        print(" No of mobiles = " ,self.no_of_mob )
        print(" Dad mobiles =  " , self.dad_mob )
        print(" Mom mobiles =  " , self.bro_mob )
        print(" MY 0mobiles = " , self.my_mob)

    def m1():
        print("AAg lage cls aur self mein hum humare static method mein")


f = Flat(3 , " MI" ,"OPPO" ,"Samsung")
Flat.cupboard = 2
Flat.dispStatic(3)
f.Display()
