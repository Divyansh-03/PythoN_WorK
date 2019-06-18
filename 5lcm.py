''' 
Question 7 :- 

Input two number and calculate their HCF and LCM  '''

a = int(input(" Enter 1st number "))
b = int(input(" Enter 2nd number "))

max = max(a,b)
lcm=1
while True:
	if max%a==0 and max%b==0:
		lcm = max
		break
	else:
		max=max+1
		
print( " The Lcm of given numbers " + str(a) +" and " + str(b) + " is " + str(lcm))

# For HCF of two numbers
min = min(a,b)
hcf = 1
while True:
	if a%min==0 and b%min==0:
		hcf = min
		break
	else:
		min = min-1

print( " The HCF or GCD of given numbers " + str(a) +" and " + str(b) + " is " + str(hcf))