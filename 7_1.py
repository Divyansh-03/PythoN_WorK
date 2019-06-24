''' Question 1 :-

Write a program to calculate overtime pay of 10 employees.
Overtime is paid at the rate of Rs. 12.00 per hour for every
hour worked above 40 hours. Assume that employees do not
work for fractional part of an hour '''

hours = int(input(" Enter the number of hours for which worker has worked \n "))
if hours<=40:
	print(" No Overtime Pay \n")
else:
	pay = (hours-40)*12
	print(" The overtime pay is " , Rs. pay)