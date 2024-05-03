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