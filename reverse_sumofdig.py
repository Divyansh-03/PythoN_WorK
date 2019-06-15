''' If a five-digit number is input through the keyboard, write a
program to calculate the sum of its digits.
85296
 8 + 5 + 2 + 9 + 6 = 30
(Hint: Use the modulus operator ‘%’) 

If a five-digit number is input through the keyboard, write a
program to reverse the number.
 
If a four-digit number is input through the keyboard, write a
program to obtain the sum of the first and last digit of this
number. '''



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
print(" The sum of digits of " + str(temp) + " is " + str(d1+d2+d3+d4+d5) )
print( " The reverse of " + str(temp) + "is " + str(d1*10000 + d2*1000 + d3*100 + d4*10 +d5))
print( " The sum of first and last digit of " + str(temp) + "is " + str(d1+d5))