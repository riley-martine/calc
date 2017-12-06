from functions import round_sig, get_source
from iroc import iroc
from math import sqrt, log

def sec(f, a, h):
    # Slope of secant line
    m = (f(a+h) - f(a))/h
    return lambda x: (m*(x-a))+f(a)

def der(f):
    verysmall = 0.000000001
    return lambda x: (f(x+verysmall)-f(x))/verysmall

if __name__ == '__main__':
    def f(x):
        return sqrt(x*log(3*x-2))

    # Inital value
    a = 1
    # Delta x
    h = 0.001
    s = sec(f, a, h)
    print(get_source(f))
    for i in range(1, 10):
        val = round_sig(s(i), 4)
        print(f'i: {i}, s(i): {val}')
    print('---------------------')
    d = der(f)
    for i in range(1, 10):
        val = round_sig(d(i), 4)
        print(f'i: {i}, d(i): {val}')

