from sympy import sympify, Symbol

import sympy as sp

def biseccion(f, a, b, tol):
    #x = sp.Symbol('x')
    #f = sp.lambdify(x, f_expr)

    if f(a) * f(b) >= 0:
        return None, "El método de bisección no es aplicable en el intervalo dado."

    iter_count = 0
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint, f"Raíz exacta encontrada en x = {midpoint:.6f}"
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iter_count += 1

    raiz = (a + b) / 2.0
    return raiz