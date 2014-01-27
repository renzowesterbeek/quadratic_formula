#   Quadratic-Formula Python application        #
#   									  		#
#   Created in 2014 by Renzo Westerbeek 		#

import math
from Tkinter import *

def calculate():

	# Stores A, B and C #
	A = int(AEntry.get())
	B = int(BEntry.get())
	C = int(CEntry.get())

	# Calculates Discriminant #
	D = (B)**2-4*A*C

	# If D < 0 -> No solution #
	if D < 0:
		answer.set("There is no solution...")
	else:
		# Executes ABC-Formula #
		X1 = (-B-math.sqrt(D))/(2*A)
		X2 = (-B+math.sqrt(D))/(2*A)

		# If D = 0 -> Only 1 solution #
		if X1 == X2:
			discriminant.set("Discriminant: " + str(D))
			answer.set("X = " + str(X1))
		else:
			discriminant.set("Discriminant: " + str(D))
			answer.set("X = " + str(X1) + " of X = " + str(X2))
		
# Basic window configuration #
app = Tk()
app.geometry("400x300")
app.title("Quadratic Formula Calculator")

welcomeText = IntVar()
welcomeText.set("Put in your A, B and C values...")
welcomeTextLabel = Label(app, textvariable=welcomeText)
welcomeTextLabel.pack()

# A input #
AText = IntVar()
AText.set("A:")
ALabel = Label(app, textvariable=AText)
ALabel.pack()

AEntry = Entry(app)
AEntry.pack()

# B input #
BText = IntVar()
BText.set("B:")
BLabel = Label(app, textvariable=BText)
BLabel.pack()

BEntry = Entry(app)
BEntry.pack()

# C input #
CText = IntVar()
CText.set("C:")
CLabel = Label(app, textvariable=CText)
CLabel.pack()

CEntry = Entry(app)
CEntry.pack()

# Button #
button1 = Button(app, text="Calculate!", command=calculate)
button1.pack()

# Output Labels #
discriminant = IntVar()
discriminant.set("")
discriminantLabel = Label(app, textvariable=discriminant)
discriminantLabel.pack()

# Output Labels #
answer = IntVar()
answer.set("")
answerLabel = Label(app, textvariable=answer)
answerLabel.pack()

app.mainloop()
