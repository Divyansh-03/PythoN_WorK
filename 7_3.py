''' Write a program to print out all Armstrong numbers between
1 and 500. If sum of cubes of each digit of the number is
equal to the number itself, then the number is called an
Armstrong number. For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5
* 5 ) + ( 3 * 3 * 3 ) '''

def check(i):
	n = i
	temp = n
	d1 = temp%10
	temp = temp//10
	d2= temp%10
	temp = temp//10
	d3 = temp 

	if d1**3 + d2**3 + d3**3 == n:
		print(" The Armstrong Numbers are : ",n)
	else:
		pass
# CMD shows only last 298 lines .
i = 1
while i<=500:
	check(i)
	i = i+1
	