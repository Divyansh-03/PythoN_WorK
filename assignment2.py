''' Question:- Input a Number and Display it in words according to International.

Input :- 315121810

Output :- Three hundred and fifteen million, 
one hundred and twenty-one thousand, eight hundred and ten '''
ones_place = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
		"Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens_place = ['','','Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninty'] 
str1=""
def convert(num):
	if num<20 and num>=0:
		str1= ones_place[num] 
	elif num<100 and num>19:
		str1= tens_place[(num//10)] + " " + ones_place[(num%10)]  
	elif num>=100 and num<1000:
		str1= convert(num//100) + " Hundred " + convert(num%100) 
	elif num>=1000 and num<100000:
		str1= convert(num//1000) + " Thousand " + convert(num%1000) 
	elif num>=100000 and num<101000:
		str1= convert(num//100000) + " Hundred Thousand " + convert(num%100000) 
	elif num>100999 and num<1000000: 
		str1= convert(num//100000) + " Hundred " + convert(num%100000) 
	elif num>=1000000 and num<1000000000:
		str1= convert(num//1000000) + " Million " + convert(num%1000000) 
	elif num>=1000000000 and num<1000000000000:
		str1= convert(num//1000000000) + " Billion " + convert(num%1000000000)
	return str1
#num = 999999999
num = int(input(" Enter any number "))
if num==0:
	print(" Zero ")
elif num<0:
	print(" Enter a valid number ")
else:
	str2=convert(num)
	print (str2)