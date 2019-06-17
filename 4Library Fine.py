''' A library charges a fine for every book returned late. 
For first 5 days the fine is 50 paise, for 6-10 days fine is 
one rupee and
above 10 days fine is 5 rupees. If you return the book after 30
days your membership will be cancelled. Write a program to
accept the number of days the member is late to return the
book and display the fine or the appropriate message'''

late_days = int(input(" Enter number of late days "))
if late_days <=5:
	fine = late_days*0.50
	print(" The Total Fine is " + str( fine))
elif late_days>5 and late_days <=10 :
	fine = late_days*1.0
	print(" The Total Fine is " + str( fine))
elif late_days >10 and late_days<=30 :
	fine = late_days *10.0
	print(" The Total Fine is " + str( fine))
else:
	print(" Membership cancelled ")