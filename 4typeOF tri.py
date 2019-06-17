''' If the three sides of a triangle are entered through the
keyboard, write a program to check whether the triangle is
isosceles, equilateral, scalene or right angled triangle. '''

a1= int(input(" Enter the 1st angle of the triangle "))
a2= int(input(" Enter the 2nd angle of the triangle "))
a3= int(input(" Enter the 3rd angle of the triangle "))

if a1==a2 and a2==a3:
	print(" The triangle is equilateral ")
elif a1==90 or a2==90 or a3==90:
	print(" The traingle is Right Angled ")
elif a1!=a2 and a2!=a3:
	print(" The traingle is Scalene ")
else:
	print(" The traingle is Isoceless ")