from aroc import aroc
from math import log10, floor, sin
from tabulate import tabulate
from inspect import getsourcelines


def round_sig(x, sig=2):
    if x == 0:
        return x
    if isinstance(x, complex):
        return "Complex"
    return round(x, sig-int(floor(log10(abs(x))))-1)


def power(x, power):
    if x >= 0:
        return x**power
    else:
        return -(-x)**power


if __name__ == "__main__":
#    values = [1, 0.1, 0.01, 0.001, -0.001, -0.01, -0.1, -1]
    values = [2, 1, .5, .01, 0.00000001, -.01, -.5, -1, -2]
    functions = [
        (lambda x: x**2, .5),
        (lambda x: .5*sin(x)+2, 0),
        (lambda x: 1/x, -4),
        (lambda x: power(x, (1./3.)), 0),
        (lambda x: (power((x-1), (2./3))) - x, 1),
        (lambda x: (power((x-1), (2./3))) - x, 0),
        (lambda x: ((-3*abs(x+2))+6), 2),
        (lambda x: (-3*abs(x+2))+6, -2),
    ]

    for row in functions:
        f, x1 = row
        d = []
        for h in values:
            x2 = x1+h
            m = aroc(f, x1, x2)
            m = round_sig(m, 4)
            #b = f(x1) - (m * x1)
            #b = round_sig(b, 4)
            #print(f"h = {h}")
            #print(f"m = {m}")
            d.append( (h, (x1, round_sig(f(x1), 4)), (x2, round_sig(f(x2), 4)), m) )
            #print(f"Line equation: y={m}x+({b})")
            #print('------------------------------')
  
        print('\n')
        print(getsourcelines(f)[0][0].strip()[11:-2])
        print(tabulate(d, headers=["delta x", "(x1, f(x1)", "x2, f(x2)",  "AROC"]))
       

   # while True:
   #     x1, x2 = [float(x) for x in input("x1, x2: ").split(', ')]
   #     m = aroc(f, x1, x2)
   #     b = f(x1) - (m * x1)
   #     print(f"Line equation: y={m}x+{b}")

