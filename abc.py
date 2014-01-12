import math

# Stores ABC #
A = input("A: ")
B = input("B: ")
C = input("C: ")

# Calculates Discriminant #
D = (B)**2-4*A*C

# There is no solution if D < 0 #
if D < 0:
	print ""
	print "No solution..."
	print ""
else:
	# Executes ABC-Formule #
	X1 = (-B-math.sqrt(D))/(2*A)
	X2 = (-B+math.sqrt(D))/(2*A)

	# Prints results to screen #

	if X1 == X2:
		print ""
		print "Discriminant: " + str(D)
		print "X = " + str(X1)
		print ""
	else:
		print ""
		print "Discriminant: " + str(D)
		print "X = " + str(X1) + " of X = " + str(X2)
		print ""