"""Funciones auxiliares que sirvan en varios lugares del código, como funciones para graficar, validar entradas, etc."""
class FuncionesAuxiliares:

    def capturar_ecuacion():
     # Capturar la ecuación ingresada por el usuario
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
        print (ecuacion_str)
        
