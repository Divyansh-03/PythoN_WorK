''' Question 9 :-

Input Any Number and display its table

2

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
...
2 * 10 = 20

5 * 4 * 3 '''

num = int(input( "\n Enter any number to display its Table \n \n"))
print("\n \n The Table of given number  " + str(num) + " is \n")
i=1
pro=1
while i<=10:
	pro = num * i
	print(" " +str(num)+" * "+str(i)+" = "+str(pro)+"\n")
	i=i+1
