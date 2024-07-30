import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from GUI.calculadora import center_window
from methods.minimosCuadrados import minimos_cuadrados

def construir_leyenda(coeficientes):
   
    terms = []
    degree = len(coeficientes) - 1
    for i, coef in enumerate(coeficientes):
        power = degree - i
        if coef != 0:
            if power == 0:
                terms.append(f"{coef:.2f}")
            elif power == 1:
                terms.append(f"{coef:.2f}x")
            else:
                terms.append(f"{coef:.2f}x^{power}")
    leyenda = " + ".join(terms)
    return f"y = {leyenda}"

def graficar_minimos_cuadrados(x, y, coeficientes):
    plt.scatter(x, y, color="red", label="Datos")
    
    x_fit = np.linspace(min(x), max(x), 1000)
    y_fit = np.polyval(coeficientes, x_fit)
    leyenda = construir_leyenda(coeficientes)
    plt.plot(x_fit, y_fit, color="blue", label=leyenda)
    
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Metodo de Mínimos Cuadrados")
    plt.legend()
    plt.grid(True)
    plt.show()

def graf_minimos():
    def add_point():
        try:
            x = float(x_entry.get())
            y = float(y_entry.get())
            points.append((x, y))
            messagebox.showinfo("Info", f"Punto ({x}, {y}) agregado.")
            x_entry.delete(0, tk.END)
            y_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos.")

    def calculate():
        if len(points) < 2:
            messagebox.showerror("Error", "Se necesitan al menos dos puntos.")
            return
        
        x, y = zip(*points)
        try:
            degree = int(degree_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un grado válido.")
            return
        
        coeficientes = minimos_cuadrados(x, y, degree)
        root.destroy()
        graficar_minimos_cuadrados(np.array(x), np.array(y), coeficientes)

    root = tk.Tk()
    root.title("Mínimos Cuadrados")
    window_width = 800
    window_height = 430
    root.geometry(f"{window_width}x{window_height}")
    center_window(root, window_width, window_height)
    root.resizable(False, False)
    
    points = []

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_columnconfigure(0, weight=1)

    label = tk.Label(root, text="Ingrese los puntos (x, y):")
    label.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

    x_entry = tk.Entry(root)
    x_entry.grid(row=1, column=0, padx=10, pady=5)
    x_entry.insert(0, "x")

    y_entry = tk.Entry(root)
    y_entry.grid(row=2, column=0, padx=10, pady=5)
    y_entry.insert(0, "y")

    add_button = tk.Button(root, text="Agregar Punto", command=add_point)
    add_button.grid(row=3, column=0, padx=10, pady=5)

    degree_label = tk.Label(root, text="Grado del polinomio:")
    degree_label.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

    degree_entry = tk.Entry(root)
    degree_entry.grid(row=5, column=0, padx=10, pady=5)
    degree_entry.insert(0, "1")

    calculate_button = tk.Button(root, text="Calcular y Graficar", command=calculate, bg="#4CAF50", fg="white")
    calculate_button.grid(row=6, column=0, padx=10, pady=10)

    root.mainloop()
