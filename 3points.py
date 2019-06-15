''' Given three points (x1, y1), (x2, y2) and (x3, y3), write a
program to check if all the three points fall on one straight line. '''


x1 = int(input(" Enter 1st x coordinate "))
y1 = int(input(" Enter 1st y coordinate "))
x2 = int(input(" Enter 2nd x coordinate "))
y2 = int(input(" Enter 2nd y coordinate "))
x3 = int(input(" Enter 3rd x coordinate "))
y3 = int(input(" Enter 3rd y coordinate "))
if (y2-y1)*(x3-x1) - (x2-x1)*(y3-y1)==0 : 
	print(" The 3 points lie on a straight line ")
else:
	print(" The 3 points do not lie on a straight line ")