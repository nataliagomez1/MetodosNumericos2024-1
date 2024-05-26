import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify, sympify

from methods.secante import secante

def graficar(ecuacion, x0, x1):
    try:
        
        x = symbols('x')
        expr = sympify(ecuacion)

        
        f = lambdify(x, expr, 'numpy')

        
        raiz = secante(f, x0, x1)

         
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)

        
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {ecuacion}')

        
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

       
        plt.scatter([raiz], [f(raiz)], color='red', zorder=5)
        plt.text(raiz, f(raiz), f'Raíz: ({raiz:.2f}, {f(raiz):.2f})', fontsize=12, verticalalignment='bottom')

         
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Gráfico de la función\nf(x) = {ecuacion}\nRaíz encontrada: ({raiz:.2f}, {f(raiz):.2f})')

        
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Error al evaluar la ecuación: {e}")

def graficar_ecuacion():
    ventana = tk.Tk()
    ventana.title("Graficador de Ecuaciones")
    ventana.geometry("400x300")
    ventana.configure(bg="#f0f0f0")

    etiqueta = tk.Label(ventana, text="Ingrese la ecuación en términos de x:", bg="#f0f0f0")
    etiqueta.pack(pady=10)

    entrada_ecuacion = tk.Entry(ventana, width=30)
    entrada_ecuacion.pack(pady=10)

    etiqueta_x0 = tk.Label(ventana, text="Ingrese el punto inicial x0:", bg="#f0f0f0")
    etiqueta_x0.pack(pady=10)

    entrada_x0 = tk.Entry(ventana, width=30)
    entrada_x0.pack(pady=10)

    etiqueta_x1 = tk.Label(ventana, text="Ingrese el punto inicial x1:", bg="#f0f0f0")
    etiqueta_x1.pack(pady=10)

    entrada_x1 = tk.Entry(ventana, width=30)
    entrada_x1.pack(pady=10)

    def on_graficar():
        ecuacion = entrada_ecuacion.get()
        try:
            x0 = float(entrada_x0.get())
            x1 = float(entrada_x1.get())
            graficar(ecuacion, x0, x1)
        except ValueError:
            messagebox.showerror("Error", "Los puntos iniciales x0 y x1 deben ser números válidos")

    boton_graficar = tk.Button(ventana, text="Graficar", command=on_graficar, bg="#4CAF50", fg="white")
    boton_graficar.pack(pady=10)

    ventana.mainloop()
