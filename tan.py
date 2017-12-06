from iroc import iroc
from functions import round_sig
from graphmpl import graph_funcs
from math import log, cos, pi, sqrt

def f(x):
    return sqrt(x*log(3*x-2))

def tangent(f, x):
    m = iroc(f, x)
    b = f(x) - m*x
    return lambda a: m*a + b

if __name__ == "__main__":
    while True:
        x = eval(input("Tangent to function at point: "))
        tan_func = tangent(f, x)
        
        m = round_sig(iroc(f, x), 4)
        b = round_sig(f(x) - m*x, 4)
        if b < 0:
            op = '-'
        else:
            op = '+'
        b = abs(b)
        print(f"Function: y = {m}x {op} {b}")
        graph_funcs([f, tan_func], min=1, max=10)


        #do_break = False
       # while not do_break:
       #     try:
        #        a = int(input("X on tangent line: "))
         #       print(tan_func(a))
          #  except EOFError:
           #     do_break = True


