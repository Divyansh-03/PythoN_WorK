''' If a five-digit number is input through the keyboard, write a
program to print a new number by adding one to each of its
digits. For example if the number that is input is 12391 then
the output should be displayed as 23402. '''

n = int(input( " Enter a 5-digit number "))
temp = n
d1=n%10
n//=10
d2=n%10
n//=10
d3=n%10
n//=10
d4=n%10
d5=n//10
# New digits 
d1=(d1+1) %10
d2=(d2+1) %10
d3=(d3+1) %10
d4=(d4+1) %10
d5=(d5+1) %10
print(" The new number formed by " + str(temp) + " is " + str(d5)+str(d4)+str(d3)+str(d2)+str(d1))