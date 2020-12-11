import sys

TeamName = sys.argv[1]
CaptainName = sys.argv[2]
countsOfTrophy =  sys.argv[3]

a = input("Enter Team €Name");
b = input("Enter captain")
c = int(input(" Enter counts of winning trophy"))


def fun(  TeamName ,  CaptainName ,  countsOfTrophy):

    print(" The Team Name is " + str(TeamName))
    print(" The Captain Name is " + str(CaptainName))
    print(" The Count of trophy winner  is " + str(countsOfTrophy))



fun(TeamName , CaptainName , countsOfTrophy)
fun(a,b,c)


print(" My name  is ")
