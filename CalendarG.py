''' 
Input Any Day Number and Display its equivalent Day Name.

If Day is 1 then Print Monday
If Day is 2 then Print Tuesday
If Day is 3 then Print Wednesday
If Day is 4 then Print Thursday
If Day is 5 then Print Friday
If Day is 6 then Print Saturday
If Day is 7 then Print Sunday
If other day is specified then print INvalid Day '''

day_num = int(input(" Enter day number "))

if day_num ==1 :
	print(" Monday ")
if day_num ==2 :
	print(" Tuesday ")
if day_num ==3 :
	print(" Wednesday ")
if day_num ==4 :
	print(" Thursday ")
if day_num ==5 :
	print(" Friday ")
if day_num ==6 :
	print(" Saturday ")
if day_num ==7 :
	print(" Sunday ")
if day_num <=0 or day_num > 7 :
	print(" Invalid day number ")