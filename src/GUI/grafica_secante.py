import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify, sympify
from GUI.calculadora import center_window,teclado
from methods.secante import secante


def graficar(ecuacion, x0, x1):
    try:
        x = symbols('x')
        expr = sympify(ecuacion)

        f = lambdify(x, expr, 'numpy')

        x_vals_secante, y_vals_secante = secante(f, x0, x1, return_points=True)

        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)

        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {ecuacion}')

        if x_vals_secante:
            for i in range(len(x_vals_secante) - 1):
                plt.plot(
                    [x_vals_secante[i], x_vals_secante[i+1]], 
                    [y_vals_secante[i], y_vals_secante[i+1]], 
                    'r--', 
                    label='Secante' if i == 0 else ""  
                )

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        raiz = x_vals_secante[-1] if x_vals_secante else None
        if raiz is not None:
            plt.scatter([raiz], [f(raiz)], color='red', zorder=5)
            plt.text(raiz, f(raiz), f'Raíz: ({raiz:.2f}, {f(raiz):.2f})', fontsize=12, verticalalignment='bottom')

        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Gráfico de la función\nf(x) = {ecuacion}\nRaíz encontrada: ({raiz:.2f}, {f(raiz):.2f})' if raiz else 'Gráfico de la función')

        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Error al evaluar la ecuación: {e}")

def graficar_ecuacion():
    ventana = tk.Tk()
    ventana.title("Graficador de Ecuaciones")
    window_width = 800
    window_height = 430
    ventana.resizable(False, False)

    ventana.geometry(f"{window_width}x{window_height}")
    center_window(ventana, window_width, window_height)

    frame_izquierdo = tk.Frame(ventana, bg="#f0f0f0")
    frame_izquierdo.pack(side=tk.LEFT, padx=20, pady=20)

    frame_derecho = tk.Frame(ventana, bg="#f0f0f0")
    frame_derecho.pack(side=tk.RIGHT, padx=20, pady=20)

    etiqueta = tk.Label(frame_izquierdo, text="Ingrese la ecuación en términos de x:", bg="#f0f0f0")
    etiqueta.grid(row=0, column=0, padx=10, pady=10)

    entrada_ecuacion = tk.Entry(frame_izquierdo, width=30)
    entrada_ecuacion.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_x0 = tk.Label(frame_izquierdo, text="Ingrese el punto inicial x0:", bg="#f0f0f0")
    etiqueta_x0.grid(row=2, column=0, padx=10, pady=10)

    entrada_x0 = tk.Entry(frame_izquierdo, width=30)
    entrada_x0.grid(row=3, column=0, padx=10, pady=10)

    etiqueta_x1 = tk.Label(frame_izquierdo, text="Ingrese el punto inicial x1:", bg="#f0f0f0")
    etiqueta_x1.grid(row=4, column=0, padx=10, pady=10)

    entrada_x1 = tk.Entry(frame_izquierdo, width=30)
    entrada_x1.grid(row=5, column=0, padx=10, pady=10)
    
    teclado(frame_derecho, entrada_ecuacion)

    def on_graficar():
        ecuacion = entrada_ecuacion.get()
        try:
            x0 = float(entrada_x0.get())
            x1 = float(entrada_x1.get())
            graficar(ecuacion, x0, x1)
        except ValueError:
            messagebox.showerror("Error", "Los puntos iniciales x0 y x1 deben ser números válidos")

    boton_graficar = tk.Button(frame_izquierdo, text="Graficar", command=on_graficar, bg="#4CAF50", fg="white")
    boton_graficar.grid(row=6, column=0, padx=10, pady=10)

    ventana.mainloop()
