"""Logica metodo PUNTO FIJO"""

import numpy as np
from sympy import symbols, Eq, lambdify, sqrt

def fixedpoint(function, derivada, x0, tolerancia=0.001, iteramax=50):
    iteration = 1
    error = 1

    while error > tolerancia and iteration < iteramax:
        try:
            x1 = function(x0)
            
            # Manejo de valores extremadamente grandes
            if abs(x1) > 1e10:
                return "El valor calculado es demasiado grande, la función puede no converger."

            x1 = round(x1, 5)

            if x1 == 0:
                return x0

            error = abs((x1 - x0) / x1)

            if error <= tolerancia:
                return "El punto de convergencia de la función es: " + str(round(x1, 4))

            # Verificación adicional de convergencia
            if abs(derivada(x0)) >= 1:
                return "La función no converge debido a la derivada >= 1 en la iteración " + str(iteration)

            x0 = x1
            iteration += 1
        except TypeError as e:
            return "Se produjo un error al calcular el punto fijo: " + str(e)
        except OverflowError as e:
            return "Se produjo un error de desbordamiento: " + str(e)

    return "No se encontró convergencia dentro del número máximo de iteraciones."

# def fixedpoint(function, derivada, x0, tolerancia=0.001, iteramax=10):

#     iteration = 1
#     error = 1

#     while (error > tolerancia and iteration < iteramax):
#         try:
#             x1 = round(function(x0), 5)

#             if x1 == 0:
#                 return x0

#             error = abs((x1 - x0) / x1)

#             if error <= tolerancia:
#                 return "El punto de convergencia de la función es: " + str(round(x1, 4))

#             if iteration == iteramax - 1:
#                 if abs(derivada(x0)) >= 1:
#                     return "La función no converge"

#             x0 = x1
#             iteration += 1
#         except TypeError as e:
#             print("Se produjo un error al calcular el punto fijo:", e)
            
