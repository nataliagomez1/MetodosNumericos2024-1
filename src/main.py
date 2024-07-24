from utils.funcionesaux import *
from methods.biseccion import bisection_method
from methods.puntofijo import fixedpoint
from GUI.grafica_puntofijo import graficar_ecuacion_punto_fijo
#from methods.jacobi import jacobi_method

from methods.newtonraphson import newton_raphson
from GUI.grafica_newton import graficar_ecuacion as newton
from methods.secante import secante 
from GUI.grafica_secante import graficar_ecuacion
from methods.gaussseidel import gauss_seidel

from methods.gaussseidel import gauss_seidel
from GUI.grafica_gauss import interfaz_grafica_gauss

from GUI.menu import Application

from GUI.grafica_trapecio import auxTrapecio

from methods.simpson import simpson
from GUI.grafica_simpson import graficar_ecuacion_simpson

import numpy as np
import matplotlib.pyplot as plt

#eliminar para que ejecute el menu normlmente
import GUI.graficar_minimos as App

def show_menu():
    print("1. Metodo Punto Fijo")
    print("2. Metodo de Biseccion")
    print("3. Metodo de Newton Raphson")
    print("4. Metodo secante")
    print("5. Metodo de Jacobi")
    print("6. Metodo de Gauss-Seidel")
    print("7. Metodo del Trapecio")
    print("8. Metodo de Simpson")
    print("0. Salir")

def choose_method():
    
    while True:
        show_menu()
        method = input("Ingrese el numero del metodo deseado: ")
        if method.isdigit():
            method = int(method)
            if method == 1:
                print("\t*** Metodo Punto Fijo ***")
                graficar_ecuacion_punto_fijo()
                #ecuacion= capturar_ecuacion
                # parametros_puntofijo = validate_parameters_puntofijo()
                # if parametros_puntofijo is not None:
                #     function, x0 = parametros_puntofijo
                #     print(fixedpoint(function, x0, toleration=0.001, iteramax=10))
                
            elif method == 2:
                print("\t*** Metodo de Biseccion ***")

                ecuacion_b = capturar_ecuacion_biseccion()
                parametros_biseccion = capturar_parametros_biseccion()
                if parametros_biseccion is not None:
                        izquierda, derecha, tol, max_iter = parametros_biseccion
                        print(bisection_method(ecuacion_b, izquierda, derecha, tol, max_iter))

            
            elif method == 3:
                print("\t*** Metodo de Newton Raphson ***")

                ecuacion = capturar_ecuacion_newton_raphson()
                parametros_newton_raphson = capturar_parametros_newton_raphson()
                if parametros_newton_raphson is not None:
                        derivada, x0 = parametros_newton_raphson
                        resultado=(newton_raphson(ecuacion, derivada, x0, tolerancia=0.001, max_iter=10 ))
                        if resultado is None:
                            print("El método de Newton-Raphson no converge para los parámetros dados.")
                        else:
                            print(f"La raíz es: {resultado}")
                            newton()
                break
            elif method == 4:  
                
                print("\t*** Método de la Secante ***")
                graficar_ecuacion()
    
                # ecuacion_funcion, ecuacion_sympy = capturar_ecuacion_secante()
                # parametros_secante = capturar_parametros_secante()
                # if parametros_secante is not None:
                #     x0, x1, tol, max_iter = parametros_secante
                    
                #     resultado_secante = secante(ecuacion_funcion, x0, x1, tol, max_iter)
                #     if resultado_secante is not None:
                #         print(f"La raíz aproximada es: {resultado_secante}")
                #     else:
                #         print("No se encontró una raíz dentro del número máximo de iteraciones permitido.")

                #         graficar_ecuacion()
                # break



            elif method == 5:
                # print("\t*** Metodo de Jacobi ***")
                
                # parametros_jacobi = capturar_parametros_jacobi()
                # if parametros_jacobi is not None:
                #     A, b, x0, tol, max_iter = parametros_jacobi
                #     x = jacobi_method(A, b, x0, tol, max_iter)
                #     if np.any(x != x0):  
                #         print(f"La solución del sistema de ecuaciones es: {x}")
                #     else:
                #         print("El método de Jacobi no logró encontrar una solución diferente de la inicial.")
                # else:
                #     print("Los parámetros no fueron capturados correctamente.")               
                
                #Esto es para cuando ya se vaya a implementar los graficos
                # Llamar al método de Jacobi y capturar la convergencia
                #x_final, convergence_data = jacobi_method(A, b, x0, tol, max_iterations)
                # Graficar la convergencia
                #graf_convergencia_jacobi(convergence_data, tol)
                

                break

            elif method == 6: 
                interfaz_grafica_gauss() 
                print("\t*** Método de Gauss-Seidel ***")
                A, b, x0, tol, max_iter = capturar_parametros_gauss_seidel()
                resultado = (gauss_seidel(A, b, x0, tol, max_iter))
                print(resultado)
                
                break
            elif method == 7:
                print("\t*** Metodo de Simpson ***")
                auxTrapecio()
                break
            elif method == 8:
                print("\t*** Metodo de Simpson ***")
                graficar_ecuacion_simpson()
                                
            
            elif method == 0:
                print("Saliendo del programa")
                break
            else :
                print("Opción inválida. Intente de nuevo.")
        else:
            print("Entrada inválida. Ingrese un número entero.")

if __name__ == "__main__":
    app = Application()
    #app.mainloop()
    
    
    #choose_method()