from math import sin, pi, cos, log, e
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import sys

func = lambda t: ((1.4*e)**(0.02*t))+(cos(2*t))**2
func = lambda t: -25*log(t+1)+120
func = cos
divisions = 50
space = (0, pi)
divsize = (space[1]-space[0])/divisions

sum = 0
for divnum in range(divisions):
    sum += func(divnum*divsize)*divsize

print("left hand sum: " + str(round(sum, 4)))


sum = 0
for divnum in range(divisions):
    sum += func((divnum+1)*divsize)*divsize

print("right hand sum: "+ str(round(sum, 4)))


sum = 0
for divnum in range(divisions):
    midpoint = (divnum*divsize) + 0.5*divsize
    sum += func(midpoint)*divsize

print("midpoint: " + str(round(sum, 4)))


def trap_area(b1, b2, h):
    return .5*(b1+b2)*h

sum = 0
for divnum in range(divisions):
    b1 = func(divnum*divsize)
    b2 = func((divnum+1)*divsize)
    h = divsize
    sum += trap_area(b1, b2, h)

print("trap: " + str(round(sum, 4)))


t = np.arange(space[0], space[1], 0.01)
s = [func(x) for x in t]

fig, ax = plt.subplots()
ax.plot(t, s)

mode = input("Which plot would you like? (lhs, rhs, mid, trap): ")

if mode == "lhs":
    # PLOT LHS
    for divnum in range(divisions):
        ax.add_patch(
            patches.Rectangle(
                (divnum*divsize, 0),   # (x, y)
                divsize,               # width
                func(divnum*divsize),  # height
                fill=False,
            )
        )

elif mode == 'rhs':  
    #PLOT RHS
    for divnum in range(divisions):
        ax.add_patch(
            patches.Rectangle(
                (divnum*divsize, 0),       # (x, y)
                divsize,                   # width
                func((divnum+1)*divsize),  # height
                fill=False,
            )
        )

elif mode == 'mid':   
    #PLOT MIDPOINT
    for divnum in range(divisions):
        ax.add_patch(
            patches.Rectangle(
                (divnum*divsize, 0),   # (x, y)
                divsize,               # width
                func(divnum*divsize+0.5*divsize),  # height
                fill=False,
            )
        )

elif mode == 'trap':    
    # PLOT TRAPEZOID
    for divnum in range(divisions):
        points = [
                  ((divnum+1)*divsize, func((divnum+1)*divsize)),
                  ((divnum+1)*divsize, 0),
                  (divnum*divsize, 0),
                  (divnum*divsize, func(divnum*divsize)),
                 ]
        ax.add_patch(
            patches.Polygon(
                points,
                fill=False,
            )
        )

else:
    print("Not a recognized mode. Goodbye!")
    sys.exit(0)

plt.show()
