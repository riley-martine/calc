from aroc import aroc
from math import sqrt

def f(x):
    return x**x

def iroc(f, x):
    return aroc(f, x, x+0.00000001)

if __name__ == '__main__':
    while True:
        x = float(input("x: "))
        print("IROC: ",  iroc(f, x))
