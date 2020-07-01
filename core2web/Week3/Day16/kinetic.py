'''Write a Program that calculates Kinetic Energy of object with given Mass & Velocity.
{Note: K.E. = ½ * m * v * v }
Input: Mass = 53kg  Velocity = 5m/s
Output: Kinetic Energy of that Object is: 662.5 '''

mass=int(input("Enter the Mass"));
velocity=int(input("Enter the Veocity"));

val=0.5


k_E=val*mass*velocity*velocity

print("Kinetic Energy of that Object is",k_E)
