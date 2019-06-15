''' Write a program to check whether a triangle is valid or not,
when the three angles of the triangle are entered through the
keyboard. A triangle is valid if the sum of all the three angles
is equal to 180 degrees. '''

n1 = float(input(" Enter 1st angle "))
n2 = float(input(" Enter 2nd angle "))
n3 = float(input(" Enter 3rd angle "))

if n1+n2+n3 ==180 :
	print(" The triangle is Valid " )
else:
	print(" The triangle is Invalid " )