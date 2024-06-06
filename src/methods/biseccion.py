import numpy as np
from sympy import symbols, Eq,lambdify

def bisection_method(func, left, right, tol, max_iter):
    """
    Encuentra la raíz de la función f en el intervalo [a, b] usando el método de bisección.
    
    Args:
        function (function): La función de la cual encontrar la raíz.
        left (float): Extremo izquierdo del intervalo.
        right (float): Extremo derecho del intervalo.
        tol (float): Tolerancia: criterio de convergencia (precisión deseada).
        max_iter (int): Número máximo de iteraciones permitidas.
        
    Returns:
        float: La aproximación de la raíz de f.
    """
    if func(left) * func(right) >= 0:
        return "La función debe tener signos opuestos en los extremos izquierdo y derecho. EL METODO DIVERGE"

    iter_count = 0
    while (right - left) / 2 > tol and iter_count < max_iter:
        medium = (left + right) / 2
        
        if func(medium) == 0:  
            return medium
        
        if func(medium) * func(left) < 0:
            right = medium  
        else:
            left = medium  
        
        iter_count += 1

    if iter_count >= max_iter:
        return "No se encontró la raíz dentro del número máximo de iteraciones. EL METODO DIVERGE"

    return (left + right) / 2