''' The distance between two cities (in km.) is input through the
keyboard. Write a program to convert and print this distance
in meters, feet, inches and centimeters. '''

dist_km = float(input("Enter distance in kilometres" ))
print(" The distance in meters is " + str(dist_km*1000.0) + " The distance in feet is "+ str(dist_km*3280.84) + " The distance in inches is " + str(dist_km*39370.1) + " The distance in centimeters is " + str(dist_km*100000.0))
