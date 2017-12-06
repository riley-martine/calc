import matplotlib.pyplot as plt

from functions import get_range_float, get_source
#from tan import tangent
from math import pi, cos
from numpy import linspace

# API scratchpad:
# 
# Things that can be done:
# * add function to graph
# * show graph



def add_func(f, min=-10, max=10):
    print(get_source(f))
    x_vals = linspace(min, max, num=100)
    y_vals = [f(x) for x in x_vals]
    plt.plot(x_vals,  y_vals)


def show_graph():
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.show()
\
def make_graph(f, min=-10, max=10):
    add_func(f, min, max)
    show_graph()

def graph_funcs(funclist, min=-10, max=10):
    for func in funclist:
        add_func(func, min, max)
    show_graph()

if __name__ == "__main__":
    from derivative import der
    f = lambda x: cos(x)
    d = der(f)
  #  t = tangent(f, pi/2)
    add_func(f)
    add_func(d)
   # add_func(t)
    show_graph()
