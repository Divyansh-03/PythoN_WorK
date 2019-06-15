'''A five-digit number is entered through the keyboard. Write a
program to obtain the reversed number and to determine
whether the original and reversed numbers are equal or not. ''' 

n = int(input( " Enter a 5-digit number " ))
temp = n
d1 = n%10 
n=n//10
d2=n%10
n=n//10
d3=n%10
n=n//10
d4=n%10
d5=n//10
rev = d1*10000 + d2*1000 + d3*100 + d4*10 +d5
print( " The reverse of " + str(temp) + " is " + str(rev))

if temp == rev :
	print(" The entered number and reverse number is equal ")
else:
	print(" The entered number and reverse number is not equal ")