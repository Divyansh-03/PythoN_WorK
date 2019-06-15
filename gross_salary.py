''' Ramesh’s basic salary is input through the keyboard. His
dearness allowance is 40% of basic salary, and house rent
allowance is 20% of basic salary. Write a program to calculate
his gross salary '''

basic_sal = int(input(" Enter Ramesh’s Basic salary in rupess "))
dearness_allowance = basic_sal *0.40
house_rent_allowance = basic_sal*0.20
print(" Ramesh’s Gross Salary is " + str(dearness_allowance + house_rent_allowance + basic_sal)) 