import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify, sympify

from methods.newtonraphson import newton_raphson

def graficar(ecuacion, x0):
    try:
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

    def on_graficar():
        ecuacion = entrada_ecuacion.get()
        try:
            x0 = float(entrada_x0.get())
            graficar(ecuacion, x0)
        except ValueError:
            messagebox.showerror("Error", "El punto inicial x0 debe ser un número válido")

    boton_graficar = tk.Button(ventana, text="Graficar", command=on_graficar, bg="#4CAF50", fg="white")
    boton_graficar.pack(pady=10)

    ventana.mainloop()