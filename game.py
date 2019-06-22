'''Question 5 :- 

Write a program for a matchstick game being played between
the computer and a user. Your program should ensure that the
computer always wins. Rules for the game are as follows:
	− There are 21 matchsticks.
	− The computer asks the player to pick 1, 2, 3, or 4
	matchsticks.
	− After the person picks, the computer does its
	picking.
	− Whoever is forced to pick up the last matchstick
	loses the game. '''
	
totalsticks=21 
pick=0
while True:
	print("\n Remaining Sticks :\n",totalsticks)
	if totalsticks == 1:
		break
	pick=int(input("\n Enter Number You Want to Pick : "))
	if pick >= 1 and pick <= 4 :
		print(" Remaining Stick :\n",totalsticks - pick )
		print(" Computer Pick : sticks =  ",5 - pick )
		totalsticks=totalsticks- 5
	else:
		print(" Stick must be picked between 1 and 4. Try Again ")

print(" You have to Pick Last Stick ie Last One.")
print(" So Computer Wins!")
