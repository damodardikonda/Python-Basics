''': Write a Program that computes Cartesian space value of a point P(x, y)
if user provides that radius and angle of that point in Polar coordinates space.
{Note: Considered 2D polar space then x & y values for Cartesian space
computed as, x = r * cos (θ) & y = r * sin (θ)}
Input: Angle = 30 & Radius: 3
Output: X = 2.59 & y = 1.5
 '''

angle=(int)input("Enter the Radius:=");
r=int(input("Enter the radius"));

if angle==30:
   x=r*0.866
   y=r*0.5

if angle==60:
   x=r*0.5
   y=r*0.866

if angle==90:
   x=r*0
   y=r*1

print("x=",x);
print("y=",y);


'''

angle=(int)input("Enter the Radius:=");
r=int(input("Enter the radius"));

if angle==30:
   x=r*0.866
   y=r*0.5

elif angle==60:
   x=r*0.5
   y=r*0.866

elif angle==90:
   x=r*0
   y=r*1

print("x=",x);
print("y=",y);

'''
