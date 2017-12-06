from math import e

def f(t, y):
    return -0.25*(t-70)

t_zero = 0
y_zero = 1

step_size = 1
step_iter = 10

for i in range(1, step_iter):
    m = f(t_zero, y_zero)
    y_zero = y_zero + step_size*m
    t_zero = t_zero + step_size
    print(f"-------------{i}-------------")
    print(f"t{i}: {t_zero}\ny{i}: {y_zero}")

