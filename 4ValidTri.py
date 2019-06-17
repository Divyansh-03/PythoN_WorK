''' If the three sides of a triangle are entered through the
keyboard, write a program to check whether the triangle is
valid or not. The triangle is valid if the sum of two sides is
greater than the largest of the three sides. '''

import math
s1= int(input(" Enter the 1st side of the triangle "))
s2= int(input(" Enter the 2nd side of the triangle "))
s3= int(input(" Enter the 3rd side of the triangle "))
max = max(s1,s2,s3)
diff = s1+s2+s3 - max
if diff>max:
	print(" The Triangle is Valid ")
else:
	print(" The Triangle is Invalid ")