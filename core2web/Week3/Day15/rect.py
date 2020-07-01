'''Write a Program to take input length and breadth of rectangle and calculate its area.
Input : 10 20
Output : Area of rectangle = 200 '''


length,breadth=[int(i) for i in input("Enter the length and breadth").split()]

area=length*breadth
print(area)
