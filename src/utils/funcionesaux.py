"""Funciones auxiliares que sirvan en varios lugares del código, como funciones para graficar, validar entradas, etc."""
from sympy import symbols, Eq, sqrt
    
def capturar_ecuacion():
    while True:
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
        ecuacion_str = input("Ingrese la ecuación: ")
        
        # Verificar si la ecuación contiene caracteres no permitidos
        if not all(caracter.isdigit() or caracter.isalpha() or caracter.isspace() or caracter in "+-*/^=()" for caracter in ecuacion_str):
                print("La ecuación contiene caracteres no permitidos. Por favor, inténtelo nuevamente.")
                continue
        try:
            ecuacion_str = ecuacion_str.replace("^", "**")  # Reemplazar ^ con ** para potencias
            x = symbols('x')
            ecuacion = Eq(eval(ecuacion_str.split('=')[0]), 0)
            return ecuacion        
        except Exception as e:
            print("Error al procesar la ecuación:", e)
            print("Por favor, inténtelo nuevamente.")
            continue
        
import sympy as sp
    
def validate_parameters_puntofijo():
    """
    Valida los parámetros necesarios para el método del punto fijo.

    Args:
        starting_point (str): Punto inicial para el método del punto fijo.
        auxiliary_function (str): Función auxiliar utilizada en el método del punto fijo.

    Returns:
        tuple or None: Una tupla que contiene la función auxiliar validada y el punto inicial convertido a float,
                       o None si ocurre algún error de validación.
    """
    function = capturar_ecuacion()
    while True:
        try:
            starting_point = float(input("Ingrese el punto inicial: "))
            #print(f"Imprimir {starting_point:.2f} función {function} ")
            return function, starting_point
        except:
            print("El dato ingresado es invalido")
            print("Ingrese datos numericos ")
            continue

def capturar_parametros_biseccion():        
    
    while True:
        
        try:
            izquierda = float(input("Ingrese el extremo izquierdo del intervalo: "))
            derecha = float(input("Ingrese el extremo derecho del intervalo: "))
        except ValueError:
            print("Los extremos del intervalo deben ser números reales. Inténtelo nuevamente.")
            continue
        
        if izquierda >= derecha:
            print("El extremo izquierdo del intervalo debe ser menor que el extremo derecho. Inténtelo nuevamente.")
            continue

        try:
            tol = float(input("Ingrese la tolerancia: "))
            max_iter = int(input("Ingrese el número máximo de iteraciones: "))
        except ValueError:
            print("La tolerancia y el número máximo de iteraciones deben ser números. Inténtelo nuevamente.")
            continue

        if tol <= 0 or max_iter <= 0:
            print("La tolerancia y el número máximo de iteraciones deben ser números positivos. Inténtelo nuevamente.")
            continue
    
        return izquierda, derecha, tol, max_iter
