''' Question 6 :-

Input any Number and calculate its Factorial
!5 = 5 * 4 * 3 * 2 * 1 '''

num = int(input(" Enter any number "))
temp = num
fact = 1
if num==0:
	fact = 1
elif num<0:
	print(" Factorial undefined ")
else:
	while temp:
		fact = fact*temp
		temp = temp-1
		
print(" The factorial of given number , " + str(num) + "! = " + str(fact))
		