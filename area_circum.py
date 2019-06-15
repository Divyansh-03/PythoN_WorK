'''The length & breadth of a rectangle and radius of a circle are
input through the keyboard. Write a program to calculate the
area & perimeter of the rectangle, and the area &
circumference of the circle. '''

length = int(input(" Enter the length in metres "))
breadth = int(input(" Enter the breadth in metres "))
radius = int(input(" Enter the radius in metres "))

print(" The Area of Rectangle is " + str(length*breadth) + " The Perimeter of Rectangle " + str(2*(length+breadth)))
print(" The Area of Circle is " + str(3.14*(radius**2)) + " The Perimeter of Circle " + str(2*3.14*radius))