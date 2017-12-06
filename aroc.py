import sys
import math

def d(x):
    return x**x
    #return (.2 * (x**3)) - (3 * x)

def aroc(func, start, end):
    deltad = func(end) - func(start)
    deltax = end - start
    return deltad/deltax

if __name__ == "__main__":
    while True:
        s, e = [float(x) for x in input("X1, X2: ").split(', ')]
        print(aroc(d, s, e))
