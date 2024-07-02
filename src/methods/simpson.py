import numpy as np

def simpson(f, a, b, n):
    # Verificar que el número de subintervalos sea par
    if n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser par")
    
    h = (b - a) / n
    suma = f(a) + f(b)
    x_vals = np.linspace(a, b, n+1)
    y_vals = f(x_vals)
    
    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)
    
    for i in range(2, n, 2):
        suma += 2 * f(a + i * h)
    
    return (h / 3) * suma, x_vals, y_vals