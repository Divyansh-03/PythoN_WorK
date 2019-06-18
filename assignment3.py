''' Input Year Until User Enter Year between 1950 to 2019.

Input Month Until User Enter Month Between 1 to 12.

Calculate Date Range
	1) 	If Month is 1 , 3 , 5 , 7 ,8, 10,12 then Date Range is 31

	2)	If Month is 4 , 6 , 9 , 11 then Date Range is 30

	3)	If Month is 2, then check year is leap or not.
		If year is leap then Date Range is 29
		If year is not leap then Date Range is 28

Input Date Until User Enter Date Between 1 to Date Range.

Let us assume, 
Year is 2019
Month is 5
Date is 25

Then Output Will Be :

On 25th May, 2019 has Saturday. '''


while True :
	year = int(input("  \n Enter Any Year : "))
	if year>=1950 and year<=2019:
		break	
	print(" Enter a Valid year ")
	
while True :
	month = int(input("  \n Enter Any Month : "))
	if month>=1 and month<=12:
		break	
	print(" Enter a Valid Month between 1 and 12")
	

if month==2:
	if year%4==0 and year%100!=0 or year%400==0:
		daterange = 29
	else :
		daterange=28
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
	daterange=31
else:
	daterange=30

while True :
	date = int(input("  \n Enter Any Date : "))
	if date>=1 and date<=daterange:
		break	
	print(" Enter a Valid Date between 1 and ",daterange)

td = ( year - 1 ) * 365
td += ( year - 1 ) // 4
td -= ( year - 1 ) // 100
td += ( year - 1 ) // 400

temp = 1

while temp<month:
	if month == 2:
		if year%4==0 and year%100!=0 or year%400==0:
			daterange = 29
			td = td + daterange
			temp = temp + 1
		else:
			daterange = 28
			td = td + daterange
			temp = temp + 1
	elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		daterange=31
		td = td + daterange
		temp = temp + 1
	else:
		daterange=30
		td = td + daterange
		temp = temp + 1

td = td + date-1
odd_days = td % 7
print(" On ")

if date == 1 or date == 21 or date == 31:
	print(str(date) + "st ")
elif date == 2 or date == 22:
	print(str(date)+"nd ")
elif date == 3 or date == 23 :
	print(str(date)+"rd ")
else:
	print(str(date)+"th ")
	
if month == 1:
	print("January ,")
elif month == 2:
	print("February ,")
elif month == 3:
	print("March ,")
elif month == 4:
	print("April ,")
elif month == 5:
	print("May ,")
elif month == 6:
	print("June ,")
elif month == 7:
	print("July ,")
elif month == 8:
	print("August ,")
elif month == 9:
	print("September ,")
elif month == 10:
	print("October ,")
elif month == 11:
	print("November ,")
else:
	print("December ,")
	
if odd_days==0:
	print(str(year)+" has Monday ")
if odd_days==1:
	print(str(year)+" has Tuesday ")
if odd_days==2:
	print(str(year)+" has Wednesday ")
if odd_days==3:
	print(str(year)+" has Thursday ")
if odd_days==4:
	print(str(year)+" has Friday ")
if odd_days==5:
	print(str(year)+" has Saturday ")
if odd_days==6:
	print(str(year)+" has Sunday ")