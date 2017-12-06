import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, plot

import numpy as np

from functions import round_sig, get_range_float


def get_graph_func(f, min=-100, max=100, step=1):
    y_values = []
    for x in get_range_float(min, max, step):
        try:
            y_values.append(f(x))
        except ZeroDivisionError:
            pass

    x_values = [x for x in range(min, max, step)]

    trace = go.Scatter(
        x = x_values,
        y = y_values,
        mode = 'lines',
    )
    
    return trace

def graph_func(f, min=-100, max=100, step=1):
    data = [get_graph_func(f, min=min, max=max, step=step)]
    return plot(data, filename='out.html')

def graph_funcs(f_list, min=-100, max=100, step=1):
    data = [get_graph_func(f, min=min, max=max, step=step) for f in f_list]
    #print(data[0])
    return plot(data, filename='out.html')



if __name__ == "__main__":
    print(list(get_range_float(-10, 10, 0.1)))
