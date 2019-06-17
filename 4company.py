''' In a company, worker efficiency is determined on the basis of
the time required for a worker to complete a particular job. If
the time taken by the worker is between 2 – 3 hours, then the
worker is said to be highly efficient. If the time required by
the worker is between 3 – 4 hours, then the worker is ordered
to improve speed. If the time taken is between 4 – 5 hours, the
worker is given training to improve his speed, and if the time
taken by the worker is more than 5 hours, then the worker has
to leave the company. If the time taken by the worker is input
through the keyboard, find the efficiency of the worker. '''

time = int(input(" Input time in hours "))
if time>=2 and time<3:
	print(" Worker is Highly Efficient ")
elif time>=3 and time<4:
	print(" Worker is Ordered to Improve Speed ")
elif time>=4 and time<5:
	print(" Worker is Trained to Improve Speed ")
else:
	print(" Worker has to leave the company ")