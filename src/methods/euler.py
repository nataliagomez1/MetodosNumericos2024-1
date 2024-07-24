import numpy as np

def euler(f, y0, x0, xf, n_intervals):
    dx = (xf - x0) / n_intervals
    x = np.linspace(x0, xf, n_intervals + 1)
    y = np.zeros(len(x))
    y[0] = y0
    
    for i in range(1, len(x)):
        y[i] = y[i-1] + dx * f(x[i-1], y[i-1])
    
    return x, y
