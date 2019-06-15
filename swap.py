''' Two numbers are input through the keyboard into two
locations C and D. Write a program to interchange the
contents of C and D. '''

c = int(input( " The current value of C is " ))
d = int(input( " The current value of D is " ))
# Without using third variable
c = c+d
d = c-d
c = c-d
print(" The new value of C is " + str(c) + "\n The new value of D is " + str(d))

# Using Third Variable
e = c
c = d
d = e 
print(" The new value of C is " + str(c) + "\n The new value of D is " + str(d))