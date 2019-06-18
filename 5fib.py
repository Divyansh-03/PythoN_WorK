''' Question 4 :-

Generate First 15 Fibonacci SEries Elements

0  1  1   2   3   5   8   13  21   34    55   ..... '''

times = 13
i = 0
j = 1
print("0 \n1")
while times:
	sum = i+j
	print (sum)
	i=j
	j=sum 
	times-=1