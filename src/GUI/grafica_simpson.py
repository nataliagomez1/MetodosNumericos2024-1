import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sympify
from methods.simpson import simpson
from GUI.calculadora import center_window, teclado, teclado_digitos

def graficar_simpson(ecuacion, a, b, n):
    try:
        ecuacion = ecuacion.replace("√", "sqrt")
        ecuacion = ecuacion.replace("e", "2.7182818284")
        x = symbols('x')
        expr = sympify(ecuacion)
        f = lambdify(x, expr, 'numpy')

        resultado = simpson(f, a, b, n)

        x_vals = np.linspace(a, b, 400)
        y_vals = f(x_vals)
        plt.subplots(figsize=(10, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {ecuacion}')

        # Rellenar el área bajo la curva
        x_fill = np.linspace(a, b, 1000)
        y_fill = f(x_fill)
        plt.fill_between(x_fill, y_fill, alpha=0.3)

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
    window_width = 580
    window_height = 630
    ventana.geometry(f"{window_width}x{window_height}")
    center_window(ventana, window_width, window_height)

    ventana.configure(bg="#f0f0f0")

    etiqueta = tk.Label(ventana, text="Ingrese la ecuación en términos de x:", bg="#f0f0f0")
    etiqueta.grid(row=0, column=2, columnspan=6)

    def validate_entry_ecu(new_value):
        allowed_chars = "0123456789x√().+-*/^e"
        for char in new_value:
            if char not in allowed_chars:
                return False
        return True

    vcmdecu = (ventana.register(validate_entry_ecu), '%P')
    entrada_ecuacion = tk.Entry(ventana, width=40, validate='key', validatecommand=vcmdecu)
    entrada_ecuacion.grid(row=1, column=2, columnspan=6)
    
    teclado(ventana,entrada_ecuacion)
    
    etiqueta_a = tk.Label(ventana, text="Ingrese el límite inferior a:", bg="#f0f0f0")
    etiqueta_a.grid(row=8, column=2, columnspan=6)

    def validate_entry_limite(new_value):
        if new_value == "":
            return True
        try:
            float(new_value)
            return True
        except ValueError:
            return False

    vcmda = (ventana.register(validate_entry_limite), '%P')
    entrada_a = tk.Entry(ventana, width=40, validate='key', validatecommand=vcmda)
    entrada_a.grid(row=9, column=2, columnspan=6)
    
    etiqueta_b = tk.Label(ventana, text="Ingrese el límite superior b:", bg="#f0f0f0")
    etiqueta_b.grid(row=10, column=2, columnspan=6)

    vcmdb = (ventana.register(validate_entry_limite), '%P')
    entrada_b = tk.Entry(ventana, width=40, validate='key', validatecommand=vcmdb)
    entrada_b.grid(row=11, column=2, columnspan=6)

    etiqueta_n = tk.Label(ventana, text="Ingrese el número de subintervalos n (par):", bg="#f0f0f0")
    etiqueta_n.grid(row=12, column=2, columnspan=6)

    
    entrada_n = tk.Entry(ventana, width=40)
    entrada_n.grid(row=13, column=2, columnspan=6)

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

    boton_graficar = tk.Button(ventana, text="Graficar", command=on_graficar, bg="#4CAF50", fg="white")
    boton_graficar.grid(row=14, column=2, columnspan=6)

    ventana.mainloop()

if __name__ == "__main__":
    graficar_ecuacion_simpson()
