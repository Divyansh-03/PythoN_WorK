''' Question 4 :-

	Input any number and check it is cool or not Number is cool
	if sum of first and last digit is equal to sum of digit 
	except first and last. 

	12113
	1 + 3 = 2 + 1 + 1 '''
		
num = int(input(" Enter any number \n"))
temp = num
sum = 0
if num>=10:
	while temp>0:
		rem = temp % 10 
		sum = sum + rem 
		temp = temp // 10
reverse = 0
temp = num		
while temp>0:
	rem = temp % 10  
	reverse = (reverse * 10) + rem 
	temp = temp // 10
sum_f_l = 0
if num<0:
	print(" Enter a Valid number ")
elif num>0 and num<10:
	sum_f_l = ((num%10) + (reverse%10))  //2
else:
	sum_f_l = (num%10) + (reverse%10)

sum_mid = sum - sum_f_l

if sum_mid==sum_f_l:
	print(" Given number " + str(num) + " is a cool number " )
else:
	print(" Given number " + str(num) + " is Not a cool number " )