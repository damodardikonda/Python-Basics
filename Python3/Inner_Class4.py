class IPL:

    def __init__(self , no_of_team, no_of_match):

        self.no_of_team = no_of_team
        self.no_of_match = no_of_match
        self.team_name = self.TEAM(11 , 6 , 5 ,5)

    def display(self):
        print("The No of Teams are = " , self.no_of_team)
        print(" The number of Matches played is " , self.no_of_match)
        self.team_name.dispTeam()


    class TEAM:

        def __init__(self , no_of_players , batsman , bawler , all_rounder):

            self.no_of_players = no_of_players

            self.batsman = batsman
            self.bawler = bawler
            self.all_rounder = all_rounder

            self.team_name = "Mumbai Indians"


        def dispTeam(self):

            print("Team Name is = " , self.team_name)
            print(" number of players = " , self.no_of_players)
            print(" Batsman = " , self.batsman)
            print("Bowler = " ,self.bawler)
            print(" All Rounders = " , self.all_rounder)


ipl = IPL(11,93)
ipl.display()
