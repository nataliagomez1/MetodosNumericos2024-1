"""Logica metodo PUNTO FIJO"""

import numpy as np
from sympy import symbols, Eq,lambdify


def fixedpoint(func, x0, toleration=0.001, iteramax=10):

    

    equation = func
    expression = equation.lhs
    x = symbols('x')
    function = lambdify(x, expression, 'numpy')


    iteration = 1
    error = 1
    previouserror = 0
    divergencecount = 0 

    while (error > toleration and iteration < iteramax):
            x1 = function(x0)
            
            if x1 == 0:
                return x0
                
            error = abs((x1 - x0) / x1)

            if error > previouserror:
                divergencecount += 1
                if divergencecount >= 10:
                     return "Con esta funcion transformada el resultado se aleja de la raiz y por lo tanto diverge."
                
            else:
                divergencecount = 0
            
            previouserror = error
            x0 = x1
            iteration += 1

    return x1
