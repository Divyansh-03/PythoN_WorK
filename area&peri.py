''' Given the length and breadth of a rectangle, write a program to
find whether the area of the rectangle is greater than its
perimeter. For example, the area of the rectangle with length = 5
and breadth = 4 is greater than its perimeter. '''


length = int(input(" Enter the length in metres "))
breadth = int(input(" Enter the breadth in metres "))
area= length*breadth
perimeter = 2*(length+breadth)
if area > perimeter: 
	print(" The Area of Rectangle is greater than perimeter" )
else: 
	print(" The Area of Rectangle is smaller than perimeter" )