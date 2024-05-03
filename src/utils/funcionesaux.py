"""Funciones auxiliares que sirvan en varios lugares del código, como funciones para graficar, validar entradas, etc."""
import sympy as sp

def validate_function(function):
    try:
        x = sp.symbols('x')
        sp.sympify(function.replace("^", "**"))
        return True
    except (sp.SympifyError, TypeError):
        return False
    
def validate_parameters_puntofijo(starting_point, auxiliary_function):
    
    if not validate_function(auxiliary_function):
        print("Error: La función auxiliar no es válida.")
        return None
    
    x = sp.symbols('x')
    function = sp.sympify(auxiliary_function.replace("^", "**"))
    
    try:
        starting_point = float(starting_point)
    except ValueError:
        print("Error: El punto inicial no es válido.")
        return None
    
    return function, starting_point