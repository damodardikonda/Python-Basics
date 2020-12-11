class Exam:

    y = 20

    def __init__(self):
        self.x = 10
        self.z = 30

    def Examcancel(self ):
        print("All Are happy")
        print(self.x)
        print(self.z)

    @classmethod
    def decisionPending(cls):
        print("Angry faces" , self.y)


e = Exam()
e.Examcancel()
Exam.decisionPending()
