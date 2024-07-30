import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify

from methods.euler import euler
from GUI.calculadora import teclado, center_window

def graficar(ecuacion, y0, t0, tf, n_intervals):
    try:
        x = symbols('x')
        y = symbols('y')
        expr = sympify(ecuacion)

        f = lambdify((x, y), expr, 'numpy')

        t_vals, y_vals = euler(f, y0, t0, tf, n_intervals)

        plt.figure(figsize=(10, 6))
        plt.plot(t_vals, y_vals, label=f'y\' = {ecuacion}')

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        plt.scatter([t0], [y0], color='red', zorder=5)
        plt.text(t0, y0, f'({t0:.2f}, {y0:.2f})', fontsize=12, verticalalignment='bottom')
        
        plt.scatter([t0, tf], [y0, y_vals[-1]], color='red', zorder=5)
        plt.text(t0, y0, f'({t0:.2f}, {y0:.2f})', fontsize=12, verticalalignment='bottom')
        plt.text(tf, y_vals[-1], f'({tf:.2f}, {y_vals[-1]:.2f})', fontsize=12, verticalalignment='bottom')

        plt.xlabel('Tiempo (t)')
        plt.ylabel('y(t)')
        plt.title(f'Gráfico de la solución usando el método de Euler\ny\' = {ecuacion}')

        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Error al evaluar la ecuación: {e}")

def graficar_ecuacion():
    ventana = tk.Tk()
    ventana.title("Graficador de Ecuaciones - Euler")
    window_width = 800
    window_height = 430
    ventana.resizable(False,False)
    ventana.geometry(f"{window_width}x{window_height}")
    center_window(ventana, window_width, window_height)
    
    frame_izquierdo = tk.Frame(ventana, bg="#f0f0f0")
    frame_izquierdo.pack(side=tk.LEFT, padx=20, pady=10)

    frame_derecho = tk.Frame(ventana, bg="#f0f0f0")
    frame_derecho.pack(side=tk.RIGHT, padx=20, pady=20)

    etiqueta = tk.Label(frame_izquierdo, text="Ingrese la ecuación en términos de x y y:", bg="#f0f0f0")
    etiqueta.pack(pady=10)

    entrada_ecuacion = tk.Entry(frame_izquierdo, width=30)
    entrada_ecuacion.pack(pady=10)

    etiqueta_y0 = tk.Label(frame_izquierdo, text="Ingrese el valor inicial y:", bg="#f0f0f0")
    etiqueta_y0.pack(pady=10)

    entrada_y0 = tk.Entry(frame_izquierdo, width=30)
    entrada_y0.pack(pady=10)

    etiqueta_x0 = tk.Label(frame_izquierdo, text="Ingrese el valor inicial x:", bg="#f0f0f0")
    etiqueta_x0.pack(pady=10)

    entrada_x0 = tk.Entry(frame_izquierdo, width=30)
    entrada_x0.pack(pady=10)

    etiqueta_xf = tk.Label(frame_izquierdo, text="Ingrese el valor final x:", bg="#f0f0f0")
    etiqueta_xf.pack(pady=10)

    entrada_xf = tk.Entry(frame_izquierdo, width=30)
    entrada_xf.pack(pady=10)

    etiqueta_n_intervals = tk.Label(frame_izquierdo, text="Ingrese el número de intervalos:", bg="#f0f0f0")
    etiqueta_n_intervals.pack(pady=10)

    entrada_n_intervals = tk.Entry(frame_izquierdo, width=30)
    entrada_n_intervals.pack(pady=10)
    
    teclado(frame_derecho, entrada_ecuacion)

    def on_graficar():
        ecuacion = entrada_ecuacion.get()
        try:
            y0 = float(entrada_y0.get())
            t0 = float(entrada_x0.get())
            tf = float(entrada_xf.get())
            n_intervals = int(entrada_n_intervals.get())
            graficar(ecuacion, y0, t0, tf, n_intervals)
        except ValueError:
            messagebox.showerror("Error", "Los valores iniciales y el número de intervalos deben ser números válidos")

    boton_graficar = tk.Button(frame_derecho, text="Graficar", command=on_graficar, bg="#4CAF50", fg="white")
    boton_graficar.grid(row=8, column=1, padx=10, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    graficar_ecuacion()
