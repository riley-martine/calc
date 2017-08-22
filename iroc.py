from aroc import aroc

def f(x):
    return x**2

def iroc(f, x):
    return aroc(f, x, x+0.00000001)

while True:
    x = float(input("x: "))
    print("IROC: ",  iroc(f, x))
