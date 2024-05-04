"""Funciones auxiliares que sirvan en varios lugares del código, como funciones para graficar, validar entradas, etc."""
class FuncionesAuxiliares:
    from sympy import symbols, Eq, sqrt
def capturar_ecuacion():
    print("Estas son las operaciones y respectivos simbolos que puede usar para escribir la ecuacion",
              "Suma: +"
              "Resta: -"
              "Multiplicacion: *"
              "Division: /"
              "Potencia: ^ o **"
              "Raiz cuadrada: sqrt()"
              "Parentesis para agrupar operaciones: ()"
              "Algunos ejemplos para que vea la utilizacion de los simbolos:"
              "     2x + 3 = 7"
              "     x^2 - 4x + 4 = 0"
              "     (3 * x + 2) / 5 = 7"
              "     sqrt(x) = 4"

              )
    ecuacion_str = input("Ingrese la ecuación")
    ecuacion_str = ecuacion_str.replace("^", "**")  # Reemplazar ^ con ** para potencias

    # Convertir la cadena de texto en una expresión simbólica
    x = symbols('x')
    ecuacion = Eq(eval(ecuacion_str.split('=')[0]), 0)

    return ecuacion        

        
import sympy as sp

def validate_function(function):
    """
    Valida si la cadena de texto representa una función matemática válida en términos de 'x'.

    Args:
        function (str): Cadena de texto que representa la función matemática.

    Returns:
        bool: True si la función es válida, False si no lo es.
    """
    try:
        x = sp.symbols('x')
        sp.sympify(function.replace("^", "**"))
        return True
    except (sp.SympifyError, TypeError):
        return False
    
def validate_parameters_puntofijo(starting_point, auxiliary_function):
    """
    Valida los parámetros necesarios para el método del punto fijo.

    Args:
        starting_point (str): Punto inicial para el método del punto fijo.
        auxiliary_function (str): Función auxiliar utilizada en el método del punto fijo.

    Returns:
        tuple or None: Una tupla que contiene la función auxiliar validada y el punto inicial convertido a float,
                       o None si ocurre algún error de validación.
    """
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