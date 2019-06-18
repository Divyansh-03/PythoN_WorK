''' Question 1 :- 

	Input any number and check it is magic or not.

	What is a magic number?
	Example: 1729

	Find the sum of digits of the given number.
	(1 + 7 + 2 + 9 => 19)
	Reverse of digit sum output.  Reverse of 19 is 91
	Find the product of digit sum and the reverse of digit sum.
	(19 X 91 = 1729)
	If the product value and the given input are same, 
	then the given number is a magic number.(19 X 91 <=> 1729)
	So, 1729 is a magic number. '''
	
num = int(input(" Enter any number \n"))
temp = num
sum=0

while temp!=0:
	rem = temp % 10
	sum += rem
	temp = temp // 10
	
reverse=0
tempo = sum
while tempo!=0:
	rem = tempo % 10 
	reverse = (reverse * 10) + rem 
	tempo = tempo // 10 
		
if reverse*sum == num:
	print(" Given Number " + str(num) + " is a Magic Number ")
else:
	print(" Given Number " + str(num) + " is Not a Magic Number ")
	