''' Question 7:-

	Input Any Number and check it is palindrome or not

	1441

	Its Reverse is 1441 and it is equal to the number.
	Such Number is Called Palindrome '''

num = int(input(" Enter any number \n"))
reverse=0
temp = num
while temp>0:
	rem = temp % 10  
	reverse = (reverse * 10) + rem 
	temp = temp // 10
if reverse == num:
	print(" The number " + str(num) + " is a Palindrome ")
else :
	print(" The number " + str(num) + " is Not a Palindrome ")