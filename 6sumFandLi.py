'''
	Input any Number and Find Out its sum of first digit and 
	last digit.
	12345

	1 + 5 = 6'''
		
num = int(input(" Enter any number \n"))
reverse=0
temp = num
while temp>0:
	rem = temp % 10  
	reverse = (reverse * 10) + rem 
	temp = temp // 10
sum = 0
if num<0:
	print(" Enter a Valid number ")
elif num>0 and num<10:
	sum = ((num%10) + (reverse%10))  //2
	print(" The sum of Only First and Last digits of the Given number :" + str(num) +" is \n" + str(sum))
else:
	sum = (num%10) + (reverse%10)
	print(" The sum of Only First and Last digits of the Given number :" + str(num) +" is \n" + str(sum))

