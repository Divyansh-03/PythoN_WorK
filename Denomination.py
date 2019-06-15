''' A cashier has currency notes of denominations 10, 50 and
100. If the amount to be withdrawn is input through the
keyboard in hundreds, find the total number of currency notes
of each denomination the cashier will have to give to the
withdrawer. '''

amount = int(input(" Enter the Total Amount in Hundreds "))
notes_in_10 = amount/10
notes_in_50 = amount/50
notes_in_100 = amount/100
print(" Notes of 10Rs. " + str(notes_in_10) + "\n Notes of 50Rs. " + str(notes_in_50) + "\n Notes of 100Rs. " + str(notes_in_100) )  