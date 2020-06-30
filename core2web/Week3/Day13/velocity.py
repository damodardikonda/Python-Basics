'''Write a Program to calculate Velocity of particle in the space having Distance & Time Entered By User.
Input:
 Distance: 100m
 Time:  20sec
Output: The Velocity of a Particle roaming In space is 5m/s. '''

#Distance=int(input("Enter the Distance"));
#Time=int(input("Enter The Time"));

#velocity=Distance/Time;
#print("The Velocity of a Particle roaming In space is {}m/s.".format(velocity))

Distance,Time=[int(i) for i in range("Enter the Distance and Time").split()]
velocity=Distance/Time;
print("The Velocity of a Particle roaming In space is {}m/s.".format(velocity))
