from utils.funcionesaux import *
from methods.biseccion import bisection_method
from methods.puntofijo import fixedpoint
from methods.secante import secante 
from GUI.grafica_secante import graficar_ecuacion

import numpy as np
import matplotlib.pyplot as plt

def show_menu():
    print("1. Metodo Punto Fijo")
    print("2. Metodo de Biseccion")
    print("3. Metodo secante")
    print("0. Salir")

def choose_method():
    
    while True:
        show_menu()
        method = input("Ingrese el numero del metodo deseado: ")
        if method.isdigit():
            method = int(method)
            if method == 1:
                print("\t*** Metodo Punto Fijo ***")
                
                #ecuacion= capturar_ecuacion
                parametros_puntofijo = validate_parameters_puntofijo()
                if parametros_puntofijo is not None:
                    function, x0 = parametros_puntofijo
                    print(fixedpoint(function, x0, toleration=0.01, iteramax=100))
                
            elif method == 2:
                print("\t*** Metodo de Biseccion ***")

                ecuacion_b = capturar_ecuacion()
                parametros_biseccion = capturar_parametros_biseccion()
                if parametros_biseccion is not None:
                        izquierda, derecha, tol, max_iter = parametros_biseccion
                        print(bisection_method(ecuacion_b, izquierda, derecha, tol, max_iter))

            elif method ==3:
                graficar_ecuacion()

                break
            elif method == 4:  
                
                print("\t*** Método de la Secante ***")
    
                ecuacion_s = capturar_ecuacion()
                parametros_secante = capturar_parametros_secante()
                if parametros_secante is not None:
                    x0, x1, tol, max_iter = parametros_secante
                    def f(x):
                        return ecuacion_s.subs(symbols('x'), x).evalf()

                    resultado_secante = secante(f, x0, x1, tol, max_iter)
                    if resultado_secante is not None:
                        print(f"La raíz aproximada es: {resultado_secante}")
                    else:
                        print("No se encontró una raíz dentro del número máximo de iteraciones permitido.")
            elif method == 0:
                print("Saliendo del programa")
                break
            else :
                print("Opción inválida. Intente de nuevo.")
        else:
            print("Entrada inválida. Ingrese un número entero.")

if __name__ == "__main__":
    choose_method()