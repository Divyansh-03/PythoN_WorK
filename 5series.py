''' Print Given Series 20 Elements

0		3			8		15			24				35 48 63 80 93 ....

0   0 + 3 		3 + (3+2)	8+ 3+2+2	15 + 3+2+2+2   15 + 3+2+2+2+2  '''


times = 17
new = 0
i = 0
j = 3
k = 8
inc=2
print( str(i)+"\n \n"+ str(j) +"\n \n"+str(k)+" \n" )
while times:
	prev = k
	new = prev + 5 + inc
	k = new 
	inc = inc +2
	print(str(new)+"\n")
	times=times-1 