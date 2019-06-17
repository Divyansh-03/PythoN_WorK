'''  Any year is entered through the keyboard, write a program to
determine whether the year is leap or not. Use the logical
operators && and ||. '''

year = int(input( " Enter an year "))

if year%4==0 and (year%100!=0 or year%400==0) :
	print(" It is a Leap Year" )
else:
	print(" It is not a Leap Year ")
