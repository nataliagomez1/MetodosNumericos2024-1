import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify

from methods.puntofijo import fixedpoint
from GUI.calculadora import teclado,center_window

def graficar_punto_fijo(ecuacion, x0):
    try:
        ecuacion = ecuacion.replace("√", "sqrt")
        ecuacion = ecuacion.replace("e", "2.7182818284")
        x = symbols('x')
        expr = sympify(ecuacion)
        f = lambdify(x, expr, 'numpy')
        
        derivada_expr = expr.diff(x)
        df = lambdify(x, derivada_expr, 'numpy')

        resultado = fixedpoint(f, df, x0)
        
        try:
            punto_fijo = float(resultado.split(': ')[-1])
        except ValueError:
            punto_fijo = None

        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)
        plt.subplots(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {ecuacion}')

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        if punto_fijo is not None:
            plt.scatter([punto_fijo], [f(punto_fijo)], color='red', zorder=5)
            plt.text(punto_fijo, f(punto_fijo), f'Punto Fijo: ({punto_fijo:.2f}, {f(punto_fijo):.2f})', fontsize=12, verticalalignment='bottom')

        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Gráfico de la función\nf(x) = {ecuacion}\n{resultado}')

        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Error al evaluar la ecuación: {e}")

def graficar_ecuacion_punto_fijo():
    ventana = tk.Tk()
    ventana.title("Graficador de Ecuaciones - Punto Fijo")
    window_width = 800
    window_height = 430
    ventana.geometry(f"{window_width}x{window_height}")
    center_window(ventana, window_width, window_height)

    frame_izquierdo = tk.Frame(ventana, bg="#f0f0f0")
    frame_izquierdo.pack(side=tk.LEFT, padx=20, pady=20)

    frame_derecho = tk.Frame(ventana, bg="#f0f0f0")
    frame_derecho.pack(side=tk.RIGHT, padx=20, pady=20)

    etiqueta_ecuacion = tk.Label(frame_izquierdo, text="Ingrese la ecuación en términos de x:", bg="#f0f0f0")
    etiqueta_ecuacion.grid(row=0, column=0, padx=10, pady=10)

    entrada_ecuacion = tk.Entry(frame_izquierdo, width=40)
    entrada_ecuacion.grid(row=1, column=0, padx=10, pady=10)
    
    etiqueta_x0 = tk.Label(frame_izquierdo, text="Ingrese el punto inicial x0:", bg="#f0f0f0")
    etiqueta_x0.grid(row=2, column=0, padx=10, pady=10)

    entrada_x0 = tk.Entry(frame_izquierdo, width=40)
    entrada_x0.grid(row=3, column=0, padx=10, pady=10)

    teclado(frame_derecho, entrada_ecuacion)

    def on_graficar():
        ecuacion = entrada_ecuacion.get()
        try:
            x0 = float(entrada_x0.get())
            graficar_punto_fijo(ecuacion, x0)
        except ValueError:
            messagebox.showerror("Error", "El punto inicial x0 debe ser un número válido")

    boton_graficar = tk.Button(frame_izquierdo, text="Graficar", command=on_graficar, bg="#4CAF50", fg="white")
    boton_graficar.grid(row=4, column=0, padx=10, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    graficar_ecuacion_punto_fijo()
