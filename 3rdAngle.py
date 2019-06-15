''' Write a C program to find the third angle of a triangle
 if two angles are given. '''

angle1 = int(input(" Enter 1st angle in degrees "))
angle2 = int(input(" Enter 2nd angle in degrees "))
print(" The third angle is " + str(180-(angle1+angle2)))