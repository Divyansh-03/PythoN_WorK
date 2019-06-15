''' According to the Gregorian calendar, it was Monday on the
date 01/01/1900. If any year is input through the keyboard
write a program to find out what is the day on 1st January of
this year '''

year = int(input( " Enter an year "))
year = year-1
normal_years = year * 365
leap_yrs = year // 4 + year // 400 - year // 100 
total_days = normal_years + leap_yrs
odd_days = total_days%7
if odd_days==0:
	print(" On 1st January, Day is/was Monday ")
if odd_days==1:
	print(" On 1st January, Day is/was Tuesday ")
if odd_days==2:
	print(" On 1st January, Day is/was Wednesday ")
if odd_days==3:
	print(" On 1st January, Day is/was Thursday ")
if odd_days==4:
	print(" On 1st January, Day is/was Friday ")
if odd_days==5:
	print(" On 1st January, Day is/was Saturday ")
if odd_days==6:
	print(" On 1st January, Day is/was Sunday ")
if odd_days<0 or odd_days>=7:
	print(" Invalid choice ")