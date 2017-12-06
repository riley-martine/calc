import matplotlib.pyplot as plt
plt.style.use('seaborn')

def euler(f,y0,a,b,h):
    t,y = a,y0
    out = [(t, y)]
    while t <= b:
        #print("%6.3f %6.3f" % (t,y))
        t += h
        y += h * f(t,y)
        out.append( (t, y) )
    return out


def cooling(time, temp):
	return -0.25*(temp-70)

def plot_points(vals):
    plt.xlabel('x'); plt.ylabel('y')
    plt.plot(vals, 'bo-')
    #for tup in vals:
    #    plt.plot(tup[0], tup[1], 'bo')
    plt.show()


plot_points(euler(cooling, 120,0,100,1))
