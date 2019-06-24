''' Question 6 :-

Write a program to enter the numbers till the user wants and
at the end it should display the count of positive, negative and
zeros entered. '''
pos = 0
neg = 0
zero= 0
while True:
	print(" Enter 1 to Enter another number \n")
	print(" Enter 0 to Exit \n")
	choice = int(input(" Enter your choice \n"))
	if choice==1 :
		num = int(input(" Enter your number \n"))
		if num>0:
			pos = pos+1
		elif num<0:
			neg = neg+1
		else :
			zero = zero+1
	elif choice == 0:
		break
	else:
		print( " Enter Valid choice ")
print(" The number of positive numbers entered is" , pos)
print(" The number of negative numbers entered is" , neg)
print(" The number of Zero numbers entered is" , zero)
	