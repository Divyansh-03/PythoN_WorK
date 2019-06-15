''' Given the coordinates (x, y) of a center of a circle and it’s radius
and we also input another point ( x1, y1 )
write a program which will determine whether a point lies inside
the circle, on the circle or outside the circle.
(Hint: Use sqrt( ) and pow( ) functions) '''

import math
x1 = int(input(" Enter 1st x coordinate  of center of circle "))
y1 = int(input(" Enter 1st y coordinate  of center of circle "))
x2 = int(input(" Enter 2nd x coordinate  of point "))
y2 = int(input(" Enter 2nd y coordinate  of point "))
radius = int(input(" Enter radius of circle "))
if radius == math.sqrt(((x1-x2)**2) + ((y1-y2)**2)): 
	print(" The Point lies on the circle ")
elif radius > math.sqrt(((x1-x2)**2) + ((y1-y2)**2)):
	print(" The Point lies inside the circle ")
else :
	print(" The Point lies outside the circle ")
