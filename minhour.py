'''Write a C program that takes hours and minutes as input, and 
calculates the total number of minutes.

Write a program in C that takes minutes as input, 
and display the total number of hours and minutes. '''

hours = int(input(" Enter the number of hours "))
minutes = int(input(" Enter the number of minutes "))
res_in_minutes = hours *60 + minutes 
print(" The total number of minutes is " + str(res_in_minutes))
print(" The number of hours is " + str(res_in_minutes//60) + " The number of minutes is " + str(res_in_minutes%60))  