from inspect import getsource
from math import floor, log10

def get_source(f):
    return getsource(f).strip()

def round_sig(x, sig=2):
    if x == 0:
        return x
    if isinstance(x, complex):
        return "Complex"
    return round(x, sig-int(floor(log10(abs(x))))-1)

def get_range_float(min, max, step):
    curr = min
    while curr <= max:
        yield round_sig(curr, 4)
        curr += step




if __name__ == '__main__':
    f = lambda x: x**2
    print(get_source(f))
    print(list(get_range_float(-10, 10, 0.01)))
