''' Two numbers are entered through the keyboard. Write a
program to find the value of one number raised to the power
of another. '''

n1 = int(input(" Enter the 1st number \n "))
n2 = int(input(" Enter the 2nd number \n "))
i=1
val=n1

# To calculate n1 raised to n2
if n1==0 and n2==0:
	print(" Undefined Result ")
elif n1>=0 and n2>=0:
	if n2==0:
		print(" The result is ",1)
	else:		
		while i <n2 and n2>0 :
			val =  val* n1  
			i=i+1			
		print(" The result is ",val)
else:
	print(" Enter Valid Positive Indices \n")
	


