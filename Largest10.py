''' Input Ten Number and Find Out Largest One. '''

n1 = int(input(" Enter 1st number "))
n2 = int(input(" Enter 2nd number "))
n3 = int(input(" Enter 3rd number "))
n4 = int(input(" Enter 4th number "))
n5 = int(input(" Enter 5th number "))
n6 = int(input(" Enter 6th number "))
n7 = int(input(" Enter 7th number "))
n8 = int(input(" Enter 8th number "))
n9 = int(input(" Enter 9th number "))
n10 =int(input(" Enter 10th number "))

largest = n1
if n2>largest:
	largest=n2
if n3>largest:
	largest=n3
if n4>largest:
	largest=n4
if n5>largest:
	largest=n5
if n6>largest:
	largest=n6
if n7>largest:
	largest=n7
if n8>largest:
	largest=n8
if n9>largest:
	largest=n9
if n10>largest:
	largest=n10
print(" The Largest among 10 numbers is " + str(largest))	
