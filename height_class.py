''' Write a C program to accept the height of a person in centimeter and 
categorize the person according to their height. '''

height=float(input(" Enter Person's height in centimeter "))
if height<=150:
	print(" Person is Short heighted ")
else :
	if height>150 and height<=200 :
		print(" Person is Average heighted ")
	else:
		print(" Person is Tall Heighted ")