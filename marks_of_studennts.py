''' If the marks obtained by a student in five different subjects
are input through the keyboard, find out the aggregate marks
and percentage marks obtained by the student. Assume that
the maximum marks that can be obtained by a student in each
subject is 100. '''

n1= int(input(" Enter marks in 1st subject "))
n2= int(input(" Enter marks in 2nd subject "))
n3= int(input(" Enter marks in 3rd subject "))
n4= int(input(" Enter marks in 4th subject "))
n5= int(input(" Enter marks in 5th subject "))
print(" The aggregate marks are " + str(n1+n2+n3+n4+n5))
print(" The percentage is " + str((n1+n2+n3+n4+n5)//5))