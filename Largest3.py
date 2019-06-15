''' Input any three number and display which one is largest according to
given situation and result;
n1	n2	n3	Output

5	5	5	All Three Are Equal
5	5	2	First and Second Number are Largest
5	2	5	First and Third Number are Largest
2	5	5	Second and Third Number are Largest
5	1	2	First Number is Largest
5	11	2	Second Number is Largest
1	3	5	Third Number is Largest '''

n1 = int(input(" Enter 1st number "))
n2 = int(input(" Enter 2nd number "))
n3 = int(input(" Enter 3rd number "))

if n1==n2 and n2==n3 :
	print(" All Three are equal ")
else :
	if n1==n2 and n1!=n3:
		if n1>n3 :
			print(" First and Second are Largest ")
		else :
			print(" Third is Largest ")
	if n1==n3 and n3!=n2:
		if n1>n2 :
			print(" First and Third are Largest ")
		else :
			print(" Second is Largest ")
	if n2==n3 and n1!=n2:
		if n1>n2 :
			print(" First is Largest ")
		else :
			print(" Second and Third are Largest ")		
	if n1!=n2 and n2!=n3 and n1!=n3:
		if n1>n2 and n1>n3:
			print(" First Largest ")
		else :
			if n1<n2 and n2>n3:
				print(" Second Largest ")
			else :
				print(" Third Largest ")
		