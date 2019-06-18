''' Question 9 :-

	Input Any Number and add 1 to its digit.

	Input :- 12391

	Output :- 23402 '''

num = int(input(" Enter any number \n"))
temp = num
new_num = 0 
while temp>0:
	rem = temp%10 
	digit = (rem+1)%10 
	temp = temp//10 
	new_num = new_num*10 +digit 
reverse=0
tempo = new_num
while tempo>0:
	rem1 = tempo % 10   
	reverse = ( reverse * 10 ) + rem1
	tempo = tempo // 10  
print(" The New Number for Given number: " + str(num) + " is : " +  str(reverse))	