''' A certain grade of steel is graded according to the following
conditions:
(i) Hardness must be greater than 50
(ii) Carbon content must be less than 0.7
(iii) Tensile strength must be greater than 5600
The grades are as follows:
Grade is 10 if all three conditions are met
Grade is 9 if conditions (i) and (ii) are met
Grade is 8 if conditions (ii) and (iii) are met
Grade is 7 if conditions (i) and (iii) are met
Grade is 6 if only one condition is met
Grade is 5 if none of the conditions are met
Write a program, which will require the user to give values of
hardness, carbon content and tensile strength of the steel
under consideration and output the grade of the steel. '''

hardness = int(input(" Enter Hardness "))
carbon_content = float(input(" Enter Carbon Content "))
tensile_str = int(input(" Enter Tensile Strength "))
if hardness>50 and carbon_content<0.7 and tensile_str>5600:
	print(" grade=10 ")
elif hardness>50 and carbon_content<0.7:
	print(" grade=9 ")
elif carbon_content<0.7 and tensile_str>5600:
	print(" grade=8 ")
elif hardness>50 and tensile_str>5600:
	print(" grade=7 ")
elif hardness>50 or carbon_content<0.7 or tensile_str>5600:
	print(" grade=6 ")
else:
	print(" grade=5 ")