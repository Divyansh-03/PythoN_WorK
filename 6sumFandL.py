''' Input any Number and Find Out its sum of digit except 
	first and last. 
	12345
	543 

		2 + 3 + 4 = 9 '''
		
num = int(input(" Enter any number \n"))
temp = num
sum=0

if num>=10:
	while temp>0:
		rem = temp % 10 
		sum += rem 
		temp = temp // 10	
else:
	print(" Enter a Valid number \n")
if num>=10:
	sum = sum - (num%10)

reverse=0
temp = num
if num>=10:
	while temp>0:
		rem = temp % 10 
		reverse = (reverse * 10) + rem 
		temp = temp // 10
	
if num>=10:
	sum = sum - (reverse%10)	
	print(" The sum of the digits of the Given number " + str(num) + " except first and last digit is " + str(sum))


