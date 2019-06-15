''' If the ages of Ram, Shyam and Ajay are input through the
keyboard, write a program to determine the youngest of the
three. '''

n1 = int(input(" Enter Ram's age "))
n2 = int(input(" Enter Shyam's age "))
n3 = int(input(" Enter Ajay's age "))

if n1==n2 and n2==n3 :
	print(" All Three are of equal ages. ")
else :
	if n1==n2 and n1!=n3:
		if n1>n3 :
			print(" Ajay is Youngest. ")
		else :
			print(" Ram and Shyam of equal ages and youngest. ")
	if n1==n3 and n3!=n2:
		if n1>n2 :
			print(" Shyam is Youngest ")
		else :
			print(" Ram and Ajay are of equal ages and youngest. ")
	if n2==n3 and n1!=n2:
		if n1>n2 :
			print(" Shyam and Ajay are of equal ages and youngest. ")
		else :
			print(" Ram is Youngest. ")			
	if n1!=n2 and n2!=n3 and n1!=n3:
		if n1<n2 and n1<n3:
			print(" Ram is Youngest. ")
		else:
			if n2<n3 and n2<n1:
				print(" Shyam is Youngest. ")
			else:
				print(" Ajay is Youngest. ")