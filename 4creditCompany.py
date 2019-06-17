''' The policy followed by a company to process customer orders
is given by the following rules:
(a) If a customer order is less than or equal to that in stock
and has credit is OK, supply has requirement.
(b) If has credit is not OK do not supply. Send him
intimation.
(c) If has credit is Ok but the item in stock is less than has
order, supply what is in stock. Intimate to him data the
balance will be shipped. '''

credit = str(input(" Enter O for Ok credit and NO for Not Ok credit "))
stock = 100
cust_order = float(input(" Enter customer order "))
if credit=="O" and cust_order<=stock:
	print(" Supply has requirement ")
elif credit=="NO" and cust_order<=stock:
	print(" You are being intimated ")
elif credit=="O" and cust_order>stock:
	print(" You are being shipped " + str(stock) + " .Rest " + str( cust_order - stock) + " will be supplied later " )
else:
	print(" Invalid Input ")