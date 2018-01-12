"""Program for calculating Riemann sums of functions over intervals."""
from math import sin, pi, cos, log, e, sqrt
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import sys

func = lambda t: ((1.4*e)**(0.02*t))+(cos(2*t))**2
func = lambda t: -25*log(t+1)+120
divisions = 10
space = (0, 30)
divs, divsize = np.linspace(space[0], space[1], divisions, retstep=True)


def trap_area(b1, b2, h):
    return 0.5*(b1+b2)*h

t = np.linspace(space[0], space[1], 1000)
s = [func(x) for x in t]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
for ax in (ax1, ax2, ax3, ax4):
    ax.plot(t, s)


# PLOT LHS
lhs = 0
for divstart in divs:
    lhs += func(divstart)*divsize
    ax1.add_patch(
        patches.Rectangle(
            (divstart, 0),   # (x, y)
            divsize,               # width
            func(divstart),  # height
            fill=False,
        )
    )
lhs_str = "Left Hand Sum: " + str(round(lhs, 4))
print(lhs_str)
ax1.set_title(lhs_str)

#PLOT RHS
rhs = 0
for divstart in divs[:-1]:
    rhs += func(divstart+divsize)*divsize
    ax2.add_patch(
        patches.Rectangle(
            (divstart, 0),       # (x, y)
            divsize,                   # width
            func(divstart+divsize),  # height
            fill=False,
        )
    )
rhs_str = "Right Hand Sum: " + str(round(rhs, 4))
print(rhs_str)
ax2.set_title(rhs_str)

#PLOT MIDPOINT
mid = 0
for divstart in divs[:-1]:
    midpoint = divstart + 0.5*divsize
    mid += func(midpoint)*divsize
    ax3.add_patch(
        patches.Rectangle(
            (divstart, 0),   # (x, y)
            divsize,               # width
            func(divstart+0.5*divsize),  # height
            fill=False,
        )
    )
mid_str = "Midpoint Sum: " + str(round(mid, 4))
print(mid_str)
ax3.set_title(mid_str)

# PLOT TRAPEZOID
trp = 0
for divstart in divs[:-1]:
    b1 = func(divstart)
    b2 = func(divstart+divsize)
    h = divsize
    trp += trap_area(b1, b2, h)
    points = [
              (divstart+divsize, func(divstart+divsize)),
              (divstart+divsize, 0),
              (divstart, 0),
              (divstart, func(divstart)),
             ]
    ax4.add_patch(
        patches.Polygon(
            points,
            fill=False,
        )
    )
trp_str = "Trap Sum: " + str(round(trp, 4))
print(trp_str) # can also find with avg(lhs, rhs) but that's not as fun
ax4.set_title(trp_str)

plt.show()
