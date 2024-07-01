"""Logica metodo PUNTO FIJO"""

import numpy as np
from sympy import symbols, Eq, lambdify, sqrt

def fixedpoint(function, derivada, x0, tolerancia=0.001, iteramax=20):

    iteration = 1
    error = 1

    while (error > tolerancia and iteration < iteramax):
        try:
            x1 = round(function(x0), 5)

            if x1 == 0:
                return x0

            error = abs((x1 - x0) / x1)

            if error <= tolerancia:
                return "El punto de convergencia de la función es: " + str(round(x1, 4))

            if iteration == iteramax - 1:
                if abs(derivada(x0)) >= 1:
                    return "La función no converge"

            x0 = x1
            iteration += 1
        except TypeError as e:
            print("Se produjo un error al calcular el punto fijo:", e)
            
