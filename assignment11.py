str=""
num = int(input(" Enter any number "))
temp = num
rem = temp%100
if num==0:
	str=" Zero"
elif num<0:
	print(" Enter a valid number ")
elif rem==10:
	str = " Ten"
elif rem==11:
	str = " Eleven"
elif rem==12:
	str = " Twelve"
elif rem==13:
	str = " Thirteen"
elif rem==14:
	str = " Fourteen"
elif rem==15:
	str = " Fifteen"
elif rem==16:
	str = " Sixteen"
elif rem==17:
	str = " Seventeen"
elif rem==18:
	str = " Eighteen"
elif rem==19:
	str = " Nineteen"
elif rem==20:
	str = " Twenty"
else:

	temp = num
	rem = temp%10

	if rem==1:
		str=" One "
	elif rem==2:
		str=" Two "
	elif rem==3:
		str=" Three "
	elif rem==4:
		str=" Four "
	elif rem==5:
		str=" Five "
	elif rem==6:
		str=" Six "
	elif rem==7:
		str=" Seven "
	elif rem==8:
		str=" Eight "
	elif rem==9:
		str=" Nine "
	
	temp=num
	rem = temp%100
	rem=rem//10

	if rem==2:
		str=" Twenty"+str
	elif rem==3:
		str=" Thirty"+str
	elif rem==4:
		str=" Forty"+str
	elif rem==5:
		str=" Fifty"+str
	elif rem==6:
		str=" Sixty"+str
	elif rem==7:
		str=" Seventy"+str
	elif rem==8:
		str=" Eighty"+str
	elif rem==9:
		str= " Ninety"+str

temp=num
rem = temp%1000
rem=rem//100

if rem==1:
	str=" One Hundred"+str
elif rem==2:
	str=" Two Hundred"+str
elif rem==3:
	str=" Three Hundred"+str
elif rem==4:
	str=" Four Hundred"+str
elif rem==5:
	str=" Five Hundred"+str
elif rem==6:
	str=" Six Hundred"+str
elif rem==7:
	str=" Seven Hundred"+str
elif rem==8:
	str=" Eight Hundred"+str
elif rem==9:
	str= " Nine Hundred"+str

temp=num
rem = temp%100000
rem=rem//1000

if rem==10:
	str="Ten Thousand"+str 
elif rem==11:
	str="Eleven Thousand"+str
elif rem==12:
	str=" Twelve Thousand"+str
elif rem==13:
	str=" Thirteen Thousand"+str
elif rem==14:
	str=" Fourteen Thousand"+str
elif rem==15:
	str=" Fifteen Thousand"+str
elif rem==16:
	str=" Sixteen Thousand"+str
elif rem==17:
	str=" Seventeen Thousand"+str
elif rem==18:
	str= " Eighteen Thousand"+str
elif rem==19:
	str=" Nineteen Thousand"+str
elif rem==20:
	str="Twenty Thousand"+str
elif rem==30:
	str="Thirty Thousand"+str
elif rem==40:
	str="Forty Thousand"+str
elif rem==50:
	str="Fifty Thousand"+str
elif rem==60:
	str="Sixty Thousand"+str
elif rem==70:
	str="Seventy Thousand"+str
elif rem==80:
	str="Eighty Thousand"+str
elif rem==90:
	str= " Ninety Thousand"+str
else:
	temp=num
	rem = temp%10000
	rem=rem//1000

	if rem==1:
		str=" One Thousand"+str
	elif rem==2:
		str=" Two Thousand"+str
	elif rem==3:
		str=" Three Thousand"+str
	elif rem==4:
		str=" Four Thousand"+str
	elif rem==5:
		str=" Five Thousand"+str
	elif rem==6:
		str=" Six Thousand"+str
	elif rem==7:
		str=" Seven Thousand"+str
	elif rem==8:
		str=" Eight Thousand"+str
	elif rem==9:
		str= " Nine Thousand"+str
	
	temp=num
	rem = temp%100000
	rem=rem//10000
	
	if rem==2:
		str="Twenty"+str 
	elif rem==3:
		str="Thirty"+str
	elif rem==4:
		str=" Forty"+str
	elif rem==5:
		str=" Fifty"+str
	elif rem==6:
		str=" Sixty"+str
	elif rem==7:
		str=" Seventy"+str
	elif rem==8:
		str=" Eighty"+str
	elif rem==9:
		str=" Ninety"+str

temp=num
rem=temp%10000000
rem=rem//100000

if rem==10:
	str=" Ten Lakh"+str 
elif rem==11:
	str=" Eleven Lakh "+str
elif rem==12:
	str=" Twelve Lakh "+str
elif rem==13:
	str=" Thirteen Lakh "+str
elif rem==14:
	str=" Fourteen Lakh "+str
elif rem==15:
	str=" Fifteen Lakh "+str
elif rem==16:
	str=" Sixteen Lakh "+str
elif rem==17:
	str=" Seventeen Lakh "+str
elif rem==18:
	str= " Eighteen Lakh "+str
elif rem==19:
	str=" Nineteen Lakh "+str
elif rem==20:
	str=" Twenty Lakh "+str
elif rem==30:
	str=" Thirty Lakh "+str
elif rem==40:
	str=" Forty Lakh "+str
elif rem==50:
	str=" Fifty Lakh "+str
elif rem==60:
	str=" Sixty Lakh "+str
elif rem==70:
	str=" Seventy Lakh "+str
elif rem==80:
	str=" Eighty Lakh "+str
elif rem==90:
	str= " Ninety Lakh "+str
else:
	temp=num
	rem=temp%1000000
	rem=rem//100000
	
	if rem==1:
		str=" One Lakh "+str
	elif rem==2:
		str=" Two Lakh "+str
	elif rem==3:
		str=" Three Lakh "+str
	elif rem==4:
		str=" Four Lakh "+str
	elif rem==5:
		str=" Five Lakh "+str
	elif rem==6:
		str=" Six Lakh "+str
	elif rem==7:
		str=" Seven Lakh "+str
	elif rem==8:
		str=" Eight Lakh "+str
	elif rem==9:
		str= " Nine Lakh "+str
	
	temp=num
	rem=temp%10000000
	rem=rem//1000000
	
	if rem==2:
		str="Twenty "+str 
	elif rem==3:
		str="Thirty "+str
	elif rem==4:
		str=" Forty "+str
	elif rem==5:
		str=" Fifty "+str
	elif rem==6:
		str=" Sixty "+str
	elif rem==7:
		str=" Seventy "+str
	elif rem==8:
		str=" Eighty "+str
	elif rem==9:
		str=" Ninety "+str
	
temp=num
rem=temp%1000000000
rem=rem//10000000
	
if rem==10:
	str="Ten crore "+str
elif rem==11:
	str="Eleven crore "+str
elif rem==12:
	str="Twelve crore "+str
elif rem==13:
	str="Thirteen crore "+str
elif rem==14:
	str="Fourteen crore "+str
elif rem==15:
	str="Fifteen crore "+str
elif rem==16:
	str="Sixteen crore "+str
elif rem==17:
	str="Seventeen crore "+str
elif rem==18:
	str="Eighteen crore "+str
elif rem==19:
	str="Nineteen crore "+str
elif rem==20:
	str="Twenty crore "+str
elif rem==30:
	str="Thirty crore "+str
elif rem==40:
	str="Forty crore "+str
elif rem==50:
	str="Fifty crore "+str
elif rem==60:
	str="Sixty crore "+str
elif rem==70:
	str="Seventy crore "+str
elif rem==80:
	str="Eighty crore "+str
elif rem==90:
	str="Ninety crore "+str
else :
	
	temp=num
	rem=temp%100000000
	rem=rem//10000000

	if rem==1:
		str=" One Crore "+str
	elif rem==2:
		str=" Two Crore "+str
	elif rem==3:
		str=" Three Crore "+str
	elif rem==4:
		str=" Four Crore "+str
	elif rem==5:
		str=" Five Crore "+str
	elif rem==6:
		str=" Six Crore "+str
	elif rem==7:
		str=" Seven Crore "+str
	elif rem==8:
		str=" Eight Crore "+str
	elif rem==9:
		str= " Nine Crore "+str
	
	temp=num
	rem=temp%1000000000
	rem=rem//100000000
	
	if rem==2:
		str=" Twenty "+str 
	elif rem==3:
		str=" Thirty "+str
	elif rem==4:
		str=" Forty "+str
	elif rem==5:
		str=" Fifty "+str
	elif rem==6:
		str=" Sixty "+str
	elif rem==7:
		str=" Seventy "+str
	elif rem==8:
		str=" Eighty "+str
	elif rem==9:
		str=" Ninety "+str
print( str)
		