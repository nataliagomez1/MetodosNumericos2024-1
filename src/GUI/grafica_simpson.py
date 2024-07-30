import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify
from methods.simpson import simpson
from GUI.calculadora import center_window, teclado, validate_entry_ecu, validate_entry_decInt

def graficar_simpson(ecuacion, a, b, n):
    try:
        ecuacion = ecuacion.replace("√", "sqrt")
        ecuacion = ecuacion.replace("e", "2.7182818284")
        x = symbols('x')
        expr = sympify(ecuacion)
        f = lambdify(x, expr, 'numpy')

        resultado, x_vals, y_vals = simpson(f, a, b, n)
  
        plt.figure(figsize=(10, 6))

        plt.plot(x_vals, y_vals, label=f'f(x) = {ecuacion}')

        x_fill = np.linspace(a, b, 1000)
        y_fill = f(x_fill)
        plt.fill_between(x_fill, y_fill, alpha=0.3)
        
        for i in range(0, n, 2):
            xi = x_vals[i:i+3]
            yi = y_vals[i:i+3]
            x_interval = np.linspace(xi[0], xi[-1], 100)
            plt.plot(x_interval, [f(x) for x in x_interval], 'r--')  
            plt.bar(xi, [f(x) for x in xi], width=(xi[-1] - xi[0]) / 3, alpha=0.3, align='edge')

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Gráfico de la función y área bajo la curva\nf(x) = {ecuacion}\nResultado: {resultado:.4f}')

        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Error al evaluar la ecuación: {e}")

def graficar_ecuacion_simpson():
    ventana = tk.Tk()
    ventana.title("Graficador de Ecuaciones - Método de Simpson")
    window_width = 800
    window_height = 430
    ventana.resizable(False, False)
    ventana.geometry(f"{window_width}x{window_height}")
    center_window(ventana, window_width, window_height)

    ventana.configure(bg="#f0f0f0")

    frame_izquierdo = tk.Frame(ventana, bg="#f0f0f0")
    frame_izquierdo.pack(side=tk.LEFT, padx=20, pady=20)

    frame_derecho = tk.Frame(ventana, bg="#f0f0f0")
    frame_derecho.pack(side=tk.RIGHT, padx=20, pady=20)

    etiqueta_ecuacion = tk.Label(frame_izquierdo, text="Ingrese la ecuación en términos de x:", bg="#f0f0f0")
    etiqueta_ecuacion.grid(row=0, column=0, padx=10, pady=10)

    vcmdecu = (ventana.register(validate_entry_ecu), '%P')
    entrada_ecuacion = tk.Entry(frame_izquierdo, width=40, validate='key', validatecommand=vcmdecu)
    entrada_ecuacion.grid(row=1, column=0, padx=10, pady=10)

    etiqueta_a = tk.Label(frame_izquierdo, text="Ingrese el límite inferior a:", bg="#f0f0f0")
    etiqueta_a.grid(row=2, column=0, padx=10, pady=10)

    vcmda = (ventana.register(validate_entry_decInt), '%P')
    entrada_a = tk.Entry(frame_izquierdo, width=40, validate='key', validatecommand=vcmda)
    entrada_a.grid(row=3, column=0, padx=10, pady=10)

    etiqueta_b = tk.Label(frame_izquierdo, text="Ingrese el límite superior b:", bg="#f0f0f0")
    etiqueta_b.grid(row=4, column=0, padx=10, pady=10)

    vcmdb = (ventana.register(validate_entry_decInt), '%P')
    entrada_b = tk.Entry(frame_izquierdo, width=40, validate='key', validatecommand=vcmdb)
    entrada_b.grid(row=5, column=0, padx=10, pady=10)

    etiqueta_n = tk.Label(frame_izquierdo, text="Ingrese el número de subintervalos n (par):", bg="#f0f0f0")
    etiqueta_n.grid(row=6, column=0, padx=10, pady=10)

    entrada_n = tk.Entry(frame_izquierdo, width=40)
    entrada_n.grid(row=7, column=0, padx=10, pady=10)

    teclado(frame_derecho, entrada_ecuacion)

    def on_graficar():
        ecuacion = entrada_ecuacion.get()
        try:
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            n = int(entrada_n.get())
            if n > 0 and n % 2 == 0:
                graficar_simpson(ecuacion, a, b, n)
            else:
                messagebox.showerror("Error", "El número de subintervalos n debe ser un entero positivo y par.")
        except ValueError:
            messagebox.showerror("Error", "Los límites y el número de subintervalos deben ser valores válidos")

    boton_graficar = tk.Button(frame_izquierdo, text="Graficar", command=on_graficar, bg="#4CAF50", fg="white")
    boton_graficar.grid(row=8, column=0, padx=10, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    graficar_ecuacion_simpson()
