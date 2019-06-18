''' Question 5:-

Genereate First 15 Thibonacci Series Elements

0   1    1    2    4   7    13     24 ....   '''

times = 12
i = 0
j = 1
k = 1
print("0 \n1\n1")
while times:
	sum = i+j+k
	print (sum)
	i=j
	j=k
	k=sum
	times-=1