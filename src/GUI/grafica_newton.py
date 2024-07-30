import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify, sympify

from methods.newtonraphson import newton_raphson
from GUI.calculadora import teclado,center_window,validate_entry_ecu,validate_entry_decInt


def graficar(ecuacion, x0): 
    try:
        ecuacion = ecuacion.replace("√", "sqrt")
        ecuacion = ecuacion.replace("e", "2.7182818284")
        x = symbols('x')
        expr = sympify(ecuacion)
        derivada = diff(expr, x)
        
        raiz = newton_raphson(sympify(ecuacion), derivada, x0)
        
        if (raiz != None):
        
            f = lambdify(x, expr, 'numpy')
            f_prime = lambdify(x, derivada, 'numpy')

            # Encontrar la raíz usando el método de Newton-Raphson

            # Generar valores para graficar
            x_vals = np.linspace(-10, 10, 400)
            y_vals = f(x_vals)
            y_prime_vals = f_prime(x_vals)

            # Crear la gráfica
            plt.figure(figsize=(10, 6))
            plt.plot(x_vals, y_vals, label=f'f(x) = {ecuacion}')
            plt.plot(x_vals, y_prime_vals, label=f"f'(x) = {derivada}")

            # Graficar los ejes x e y
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)

            # Graficar la raíz encontrada
            plt.scatter([raiz], [f(raiz)], color='red', zorder=5)
            plt.text(raiz, f(raiz), f'Raíz: ({raiz:.2f}, {f(raiz):.2f})', fontsize=12, verticalalignment='bottom')

            # Añadir etiquetas y título
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title(f'Gráfico de la función y su derivada\nf(x) = {ecuacion}\nRaíz encontrada: ({raiz:.2f}, {f(raiz):.2f})')

            # Mostrar leyenda
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            messagebox.showinfo("No se encontro la raiz")
    except Exception as e:
        messagebox.showerror("Error", f"Error al evaluar la ecuación: {e}")

def graficar_ecuacion():
    ventana = tk.Tk()
    ventana.title("Graficador de Ecuaciones - Punto Fijo")
    window_width = 800
    window_height = 430
    ventana.resizable(False, False)

    ventana.geometry(f"{window_width}x{window_height}")
    center_window(ventana, window_width, window_height)

    frame_izquierdo = tk.Frame(ventana, bg="#f0f0f0")
    frame_izquierdo.pack(side=tk.LEFT, padx=20, pady=20)

    frame_derecho = tk.Frame(ventana, bg="#f0f0f0")
    frame_derecho.pack(side=tk.RIGHT, padx=20, pady=20)

    etiqueta_ecuacion = tk.Label(frame_izquierdo, text="Ingrese la ecuacion e terminos de x:", bg="#f0f0f0")
    etiqueta_ecuacion.grid(row=0, column=0, padx=10, pady=10)
    
    vcmdecu = (ventana.register(validate_entry_ecu), '%P')
    entrada_ecuacion = tk.Entry(frame_izquierdo, width=40, validate='key', validatecommand=vcmdecu)

    entrada_ecuacion.grid(row=1, column=0, padx=10, pady=10)
    
    etiqueta_x0 = tk.Label(frame_izquierdo, text="Ingrese el punto inicial x0:", bg="#f0f0f0")
    etiqueta_x0.grid(row=2, column=0, padx=10, pady=10)

    vcmda = (ventana.register(validate_entry_decInt), '%P')
    entrada_x0 = tk.Entry(frame_izquierdo, width=40, validate='key', validatecommand=vcmda)
    entrada_x0.grid(row=3, column=0, padx=10, pady=10)

    teclado(frame_derecho, entrada_ecuacion)

    def on_graficar():
        ecuacion = entrada_ecuacion.get()
        try:
            x0 = float(entrada_x0.get())
            ventana.destroy()
            graficar(ecuacion, x0)
        except ValueError:
            messagebox.showerror("Error", "El punto inicial x0 debe ser un número válido")

    boton_graficar = tk.Button(frame_izquierdo, text="Graficar", command=on_graficar, bg="#4CAF50", fg="white")
    boton_graficar.grid(row=4, column=0, padx=10, pady=10)


    ventana.mainloop()