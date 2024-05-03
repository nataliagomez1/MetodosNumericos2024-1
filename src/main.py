from utils.funcionesaux import *

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
                
                while True:
                    function = input("Ingrese la funcion auxiliar: ")
                    point = input("Ingrese el punto inicial: ")
                    
                    parameters = validate_parameters_puntofijo(point, function)
                    if parameters is not None:
                        f , x0 = parameters
                        #logico del codigo
                        break
                
            elif method == 2:
                print("\t*** Metodo de Biseccion ***")
            elif method == 0:
                print("Saliendo del programa")
                break
            else :
                print("Opción inválida. Intente de nuevo.")
        else:
            print("Entrada inválida. Ingrese un número entero.")

if __name__ == "__main__":
    choose_method()