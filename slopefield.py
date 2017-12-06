from tabulate import tabulate

def f(x, y):
    if y == 0:
        return 0
    return (2*x)/y


out = []
for i in range(-6, 7):
    for j in range(-6, 7):
        out.append( (i, j, f(i, j)) )

print(tabulate(out, headers=["x", "y", "m"]))
