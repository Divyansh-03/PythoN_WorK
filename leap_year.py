''' Any year is input through the keyboard. Write a program to
determine whether the year is a leap year or not.
(Hint: Use the % (modulus) operator) ''' 

year = int(input( " Enter an year "))

if year %4 ==0 :
	if year%100==0:
		if year%400==0 :
			print(" It is a Leap Year ")
		else :
			print(" It is not a Leap year ")
	else:
		print(" It is a Leap year ")
else:
	print(" It is not a Leap year ")