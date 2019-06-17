''' Question:- Input a Number and Display it in words.

Input :- 999999999

Output :- Ninty Nine Crore Ninty Nine Lac Ninty Nine Thousands
Nine Hundred Ninty Nine. '''
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
		str1= ones_place[(num//100)] + " Hundred " + convert(num%100) 
	elif num>=1000 and num<100000:
		str1= convert(num//1000) + " Thousand " + convert(num%1000) 
	elif num>=100000 and num<10000000:
		str1= convert(num//100000) + " Lac " + convert(num%100000) 
	elif num>=10000000 and num<1000000000:
		str1= convert(num//10000000) + " Crore " + convert(num%10000000)
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