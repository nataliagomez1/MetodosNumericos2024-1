from utils.funcionesaux import *
from methods.biseccion import bisection_method

def show_menu():
    print("1. Metodo Punto Fijo")
    print("2. Metodo de Biseccion")
    print("0. Salir")

def choose_method():
    while True:
        show_menu()
        method = input("Ingrese el numero del metodo deseado: ")
        if method.isdigit():
            method = int(method)
            if method == 1:
                print("\t*** Metodo Punto Fijo ***")
                
                ecuacion= capturar_ecuacion
                parametros_puntofijo = validate_parameters_puntofijo()
                if parametros_puntofijo is not None:
                    function, point = parametros_puntofijo
                
            elif method == 2:
                print("\t*** Metodo de Biseccion ***")

                ecuacion_b = capturar_ecuacion()
                parametros_biseccion = capturar_parametros_biseccion()
                if parametros_biseccion is not None:
                        izquierda, derecha, tol, max_iter = parametros_biseccion
                        bisection_method(ecuacion_b, izquierda, derecha, tol, max_iter)
            elif method == 0:
                print("Saliendo del programa")
                break
            else :
                print("Opción inválida. Intente de nuevo.")
        else:
            print("Entrada inválida. Ingrese un número entero.")

if __name__ == "__main__":
    choose_method()