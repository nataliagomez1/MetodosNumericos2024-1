import numpy as np

def minimos_cuadrados(x, y, degree=1):
    """
    Calcula los coeficientes del polinomio de mejor ajuste usando el método de mínimos cuadrados.
    """
    x = np.array(x)
    y = np.array(y)
    
    coeficientes = np.polyfit(x, y, degree)
    
    return coeficientes

