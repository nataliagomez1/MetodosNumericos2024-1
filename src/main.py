from utils.funcionesaux import *
from methods.biseccion import bisection_method
from methods.puntofijo import fixedpoint
from methods.newtonraphson import newton_raphson
from GUI.grafica_newton import graficar_ecuacion

def show_menu():
    print("1. Metodo Punto Fijo")
    print("2. Metodo de Biseccion")
    print("3. Metodo de Newton Raphson")
    print("4. ")
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
                    print(fixedpoint(function, x0, toleration=0.001, iteramax=10))
                
            elif method == 2:
                print("\t*** Metodo de Biseccion ***")

                ecuacion_b = capturar_ecuacion_biseccion()
                parametros_biseccion = capturar_parametros_biseccion()
                if parametros_biseccion is not None:
                        izquierda, derecha, tol, max_iter = parametros_biseccion
                        print(bisection_method(ecuacion_b, izquierda, derecha, tol, max_iter))
            
            elif method == 3:
                graficar_ecuacion()
                print("\t*** Metodo de Newton Raphson ***")

                ecuacion = capturar_ecuacion_newton_raphson()
                parametros_newton_raphson = capturar_parametros_newton_raphson()
                if parametros_newton_raphson is not None:
                        derivada, x0 = parametros_newton_raphson
                        resultado=(newton_raphson(ecuacion, derivada, x0, tolerancia=0.001, max_iter=10 ))
                        print(f"La raíz es: {resultado}")
           
            elif method == 4:
                mostrar=capturar_ecuacion()
                print(str(mostrar))
            
            elif method == 0:
                print("Saliendo del programa")
                break
            else :
                print("Opción inválida. Intente de nuevo.")
        else:
            print("Entrada inválida. Ingrese un número entero.")

if __name__ == "__main__":
    choose_method()