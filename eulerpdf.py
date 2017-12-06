import numpy as np
from matplotlib import pyplot as plt

xz = 0
yz = 1
xf = 10
n = 101
deltax = (xf-xz) / (n-1)

x = np.linspace(xz, xf, n)

y = np.zeros([n])
y[0] = yz
for i in range (1, n):
    y[i] = deltax *(-y[i-1] + np.sin(x[i-1]))+y[i-1]

for i in range (n):
    print(x[i], y[i])

plt.plot(x, y, 'o')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Approximate Solution with Forward Euler’s Method")
plt.show()
