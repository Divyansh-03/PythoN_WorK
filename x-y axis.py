''' Given a point (x, y), write a program to find out if it lies on the
x-axis, y-axis or at the origin, viz. (0, 0). '''

import math
x = int(input(" Enter x coordinate  of Point "))
y = int(input(" Enter y coordinate  of Point "))
if x==0 and y==0:
	print(" Point lies at the origin (0,0) ")
elif x==0 and y!=0:
	print(" Point lies at Y axis ")
elif x!=0 and y==0:
	print(" Point lies at X axis ")
else:
	print(" Point lies mid x-y axis ")