''' Write a program to find the range of a set of numbers. Range
is the difference between the smallest and biggest number in
the list.''' 

total = int(input(" Enter the number of UNIQUE and POSITIVE numbers to be entered in the list \n"))
i = total
if total>0:
	large = -9999999999999999999999999
	small =  9999999999999999999999999


	def check(num,large,small):
		if num>large:
			large = num
		else:
			small = num 
		return large,small

	while i>0:
		num = int(input(" Enter the number \n "))
		temp = num
		large,small = check(temp,large,small)
		i=i-1
	
	
	print(" The Range if given Set of numbers is :" , large - small)
	
else:
	print(" Enter Valid numbers for the list. \n")