"""Program for calculating Riemann sums of functions over intervals."""
from math import sin, pi, cos, log, e, sqrt
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import sys

func = lambda t: ((1.4*e)**(0.02*t))+(cos(2*t))**2
func = lambda t: -25*log(t+1)+120
f1 = lambda x: 1-x**2
func = lambda x: 0 if f1(x)<0 else np.sqrt(f1(x))
func = sin
divisions = 50
space = (-1*pi, pi)
divs, divsize = np.linspace(space[0], space[1], divisions, retstep=True)

sum = 0
for div in divs:
    sum += func(div)*divsize

print("left hand sum: " + str(round(sum, 4)))


sum = 0
for div in divs:
    sum += func(div+divsize)*divsize

print("right hand sum: "+ str(round(sum, 4)))


sum = 0
for div in divs:
    midpoint = div + 0.5*divsize
    sum += func(midpoint)*divsize

print("midpoint: " + str(round(sum, 4)))


def trap_area(b1, b2, h):
    return 0.5*(b1+b2)*h

sum = 0
for div in divs:
    b1 = func(div)
    b2 = func(div+divsize)
    h = divsize
    sum += trap_area(b1, b2, h)

print("trap: " + str(round(sum, 4))) # can also find with avg(lhs, rhs) but that's not as fun


t = np.linspace(space[0], space[1], 1000)
s = [func(x) for x in t]


while True:
    fig, ax = plt.subplots()
    ax.plot(t, s)
    mode = input("Which plot would you like? (lhs, rhs, mid, trap, quit): ")
    
    if mode == "lhs":
        # PLOT LHS
        for div in divs:
            ax.add_patch(
                patches.Rectangle(
                    (div, 0),   # (x, y)
                    divsize,               # width
                    func(div),  # height
                    fill=False,
                )
            )
    
    elif mode == 'rhs':  
        #PLOT RHS
        for div in divs:
            ax.add_patch(
                patches.Rectangle(
                    (div, 0),       # (x, y)
                    divsize,                   # width
                    func(div+divsize),  # height
                    fill=False,
                )
            )
    
    elif mode == 'mid':   
        #PLOT MIDPOINT
        for divstart in divs:
            ax.add_patch(
                patches.Rectangle(
                    (divstart, 0),   # (x, y)
                    divsize,               # width
                    func(divstart+0.5*divsize),  # height
                    fill=False,
                )
            )
    
    elif mode == 'trap':    
        # PLOT TRAPEZOID
        for divstart in divs:
            points = [
                      (divstart+divsize, func(divstart+divsize)),
                      (divstart+divsize, 0),
                      (divstart, 0),
                      (divstart, func(divstart)),
                     ]
            ax.add_patch(
                patches.Polygon(
                    points,
                    fill=False,
                )
            )
    
    elif mode == 'quit':
        sys.exit(0)

    else:
        print("Not a recognized mode.")
        continue
    
    plt.show()
