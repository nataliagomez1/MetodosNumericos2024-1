"""Funciones auxiliares que sirvan en varios lugares del código, como funciones para graficar, validar entradas, etc."""
from sympy import symbols, Eq, sqrt, Add
import numpy as np
    
def capturar_ecuacion_punto_fijo():
    while True:
        try:
            ecuacion_input = input("Ingrese la ecuación g(x), ecuacion despejada, en términos de x: ")
            x = sp.symbols('x')
            ecuacion_sympy = sp.sympify(ecuacion_input)
            derivada_sympy = sp.diff(ecuacion_sympy, x)
            ecuacion_funcion = sp.lambdify(x, ecuacion_sympy, 'numpy')
            derivada_funcion = sp.lambdify(x, derivada_sympy, 'numpy')
            return ecuacion_funcion, derivada_funcion
        except (sp.SympifyError, TypeError):
            print("La ecuación ingresada no es válida. Ingrese una ecuación en términos de x.")
            

def capturar_ecuacion_biseccion():
    while True:
        try:
            ecuacion_input = input("Ingrese la ecuación f(x) en términos de x: ")
            x = sp.symbols('x')
            ecuacion_sympy = sp.sympify(ecuacion_input)
            ecuacion_funcion = sp.lambdify(x, ecuacion_sympy, 'math')
            return ecuacion_funcion
        except (sp.SympifyError, TypeError):
            print("La ecuación ingresada no es válida. Ingrese una ecuación en términos de x.")




def capturar_ecuacion_newton_raphson():
    while True:
        try:
            ecuacion_input = input("Ingrese la ecuación f(x) en términos de x: ")
            x = sp.symbols('x')
            ecuacion_sympy = sp.sympify(ecuacion_input)
            return ecuacion_sympy
        except (sp.SympifyError, TypeError):
            print("La ecuación ingresada no es válida. Ingrese una ecuación en términos de x.")
        
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
    function, derivada = capturar_ecuacion_punto_fijo()
    while True:
        try:
            starting_point = float(input("Ingrese el punto inicial: "))
            #print(f"Imprimir {starting_point:.2f} función {function} ")
            return function, derivada, starting_point
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
    
def capturar_parametros_newton_raphson():
    while True:
        try:
            derivada_str = input("Introduce la ecuación derivada: ")
            derivada_str = derivada_str.replace("^", "**")  # Reemplazar ^ con ** para potencias
            x = symbols('x')
            derivada = eval(derivada_str)
            x0 = float(input("Introduce el valor inicial x0: "))
            return derivada, x0
        except Exception as e:
            print("Error al procesar los parámetros:", e)
            print("Por favor introduce los valores nuevamente.")
            continue

def capturar_parametros_secante():
    while True:
        try:
            x0 = float(input("Ingrese el primer valor inicial (x0): "))
            x1 = float(input("Ingrese el segundo valor inicial (x1): "))
            if x0 == x1:
                print("Los valores iniciales no deben ser iguales. Por favor, inténtelo nuevamente.")
                continue
            tol = float(input("Ingrese la tolerancia (por ejemplo, 0.00001): "))
            if tol <= 0:
                print("La tolerancia debe ser un número positivo. Por favor, inténtelo nuevamente.")
                continue
            max_iter = int(input("Ingrese el número máximo de iteraciones: "))
            if max_iter <= 0:
                print("El número máximo de iteraciones debe ser un entero positivo. Por favor, inténtelo nuevamente.")
                continue
            return x0, x1, tol, max_iter
        except ValueError:
            print("Entrada no válida. Por favor, ingrese valores numéricos válidos.")

def solicitar_numero_de_ecuaciones():
    while True:
        try:
            n = int(input("Ingrese el número de ecuaciones del sistema: "))
            if n <= 0:
                raise ValueError("El número de ecuaciones debe ser positivo.")
            return n
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")

def ingresar_ecuaciones():
    n = solicitar_numero_de_ecuaciones()
    variables = sp.symbols(f'x1:{n+1}')
    ecuaciones = []
    
    print(f"Ingrese {n} ecuaciones lineales en términos de las variables {variables}:")
    for i in range(n):
        while True:
            try:
                eq_str = input(f"Ecuación {i+1}: ")
                eq = sp.sympify(eq_str)
                if not eq.free_symbols.issubset(set(variables)):
                    raise ValueError("La ecuación contiene variables no válidas.")
                ecuaciones.append(eq)
                break
            except (sp.SympifyError, ValueError) as e:
                print(f"Error: {e}. Inténtalo de nuevo.")
    
    return ecuaciones, variables

def verificar_y_despejar_ecuaciones():
    ecuaciones, variables = ingresar_ecuaciones()
    despejadas = []
    for i, eq in enumerate(ecuaciones):
        try:
            var = variables[i]
            despejada = sp.solve(eq, var)
            if len(despejada) != 1:
                raise ValueError(f"No se pudo despejar una única solución para la variable {var} en la ecuación {i+1}.")
            despejadas.append(despejada[0])
        except ValueError as e:
            print(f"Error: {e}")
            return None
    return despejadas, ecuaciones, variables

def capturar_parametros_jacobi():
    while(True):
        despejadas, ecuaciones, variables = verificar_y_despejar_ecuaciones()
        if despejadas is None:
            print("Hubo un error en el despeje de las ecuaciones. Por favor, verifica las ecuaciones ingresadas")
            continue
        for i, eq in enumerate(despejadas):
            print(f"x{i+1} = {eq}")
        try:
            tol = float(input("Ingrese la tolerancia para la convergencia: "))
            if tol <= 0:
                print("La tolerancia debe ser un número positivo.")
                continue
            max_iter = int(input("Ingrese el número máximo de iteraciones: "))
            if max_iter <= 0:
                print("El número máximo de iteraciones debe ser un entero positivo.")
                continue
            A = []
            b = []
            for eq in ecuaciones:
                coeficientes = [eq.coeff(var) for var in variables]
                termino_constante = eq - sum(coef * var for coef, var in zip(coeficientes, variables))
                A.append(coeficientes)
                b.append(termino_constante)
            x0 = np.zeros(len(A))
        except ValueError as e:
            print(f"Error en los parámetros de tolerancia o número de iteraciones: {e}")
            return
        return A, b, x0, tol, max_iter
    
        
        
            