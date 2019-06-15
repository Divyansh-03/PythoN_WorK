''' If the total selling price of 15 items and the total profit earned
on them is input through the keyboard, write a program to
find the cost price of one item. '''

sp = float(input(" Enter Total Selling Price of 15 items "))
profit = float(input(" Enter Total Profit on 15 items "))
print(" The Cost price of each item is " + str((sp - profit)/15))
