''' Write a C program to read the age of a candidate and determine 
whether it is eligible for casting his/her own vote. '''

age=float(input(" Enter Candidate's age in years "))
if age>=18 :
	print("                Candidate eligible to cast his/her vote")
else :
	print("                Candidate not eligible to cast his/her vote")