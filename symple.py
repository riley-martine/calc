from sympy import *
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')
init_printing(use_unicode=True)
x, y, z, t = symbols('x y z t')
A = symbols('A')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f, g, h', cls=Function)


#expr = x**2 - (A/x)
#expr = x+( (24- (x**2 -49)**(1/2))**2 +25)**(1/2)
#der = diff(expr, x)
#print(der)

def iroc(expr, xval):
    der = diff(expr)
    roc = der.subs(x, xval)
    return roc


def tangent(expr, xval):
    """Get tangent line of y=expr(x) at x=xval."""
    x = Symbol('x')
    slope = iroc(expr, xval)
    expr = expr.subs(x, xval)
    b = expr - slope*xval
    return slope*x + b


def eulers(expr, x_val, y_val, step_size, step_iter):
    """
    expr: an equation of the form dy/dx=expr
    """


    x = Symbol('x')
    y = Symbol('y')

    steps = [(x_val, y_val)]
    for step in range(step_iter):
        iroc = expr.subs(x, x_val)
        iroc = iroc.subs(y, y_val)
    
        x_val = x_val + step_size
        y_val = y_val + step_size*iroc
        steps.append( (x_val, y_val) )
    return steps


def plot_points(vals):
    plt.xlabel('x'); plt.ylabel('y')
    for tup in vals:
        plt.plot(tup[0], tup[1], 's-')
    plt.show()


expr = -0.25*(x-70)

plot_points(eulers(expr=expr,
             x_val=0,
             y_val=120,
             step_size=1,
             step_iter=10))

