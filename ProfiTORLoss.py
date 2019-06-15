''' If cost price and selling price of an item is input through the
keyboard, write a program to determine whether the seller has
made profit or incurred loss. Also determine how much profit
he made or loss he incurred. '''

sp = float(input( " Enter Selling price of item "))
cp = float(input( " Enter Cost price of item "))
if sp>cp: print(" He made a Profit of " + str(sp-cp))
elif cp>sp: print(" He incurred a Loss of " + str(cp-sp))
else : print(" He made neither Profit nor incurred any Loss")