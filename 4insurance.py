''' An Insurance company follows following rules to calculate
premium.
(1) If a person’s health is excellent and the person is between
25 and 35 years of age and lives in a city and is a male
then the premium is Rs. 4 per thousand and his policy
amount cannot exceed Rs. 2 lakhs.
(2) If a person satisfies all the above conditions except that
the sex is female then the premium is Rs. 3 per thousand
and her policy amount cannot exceed Rs. 1 lakh.
(3) If a person’s health is poor and the person is between 25
and 35 years of age and lives in a village and is a male
then the premium is Rs. 6 per thousand and his policy
cannot exceed Rs. 10,000.
(4) In all other cases the person is not insured.
Write a program to output whether the person should be
insured or not, his/her premium rate and maximum amount
for which he/she can be insured. ''' 

health = str(input(" Enter  E for Excellent and P for Poor health "))
age = int( input(" Enter Person's age in years "))
location = str(input(" Enter C for City and V for Village "))
gender = str(input(" Enter M for Male and F for Female "))
if health=="E" and age>=25 and age<=35 and location=="C" and gender=="M" :
	print(" Premium is 4 per thousand and Policy amount cannot exceed Rs.2 lakhs ")
elif health=="E" and age>=25 and age<=35 and location=="C" and gender=="F" :
	print(" Premium is 3 per thousand and Policy amount cannot exceed Rs.1 lakh ")
elif health=="P" and age>=25 and age<=35 and location=="V" and gender=="M" :
	print(" Premium is 6 per thousand and Policy amount cannot exceed Rs. 10000 ")
else:
	print(" Person is not insured ")