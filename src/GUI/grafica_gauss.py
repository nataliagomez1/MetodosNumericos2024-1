import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from methods.gaussseidel import gauss_seidel
from GUI.calculadora import center_window

def plot_solution(A, b, x,i):
    n = len(b)
    x_vals = np.arange(1, n + 1)
    y_vals = x

    plt.figure(figsize=(10, 6))
    plt.bar(x_vals, y_vals, align='center')
    plt.xticks(x_vals, [f'x{i+1}' for i in range(n)])
    plt.xlabel('Variables')
    plt.ylabel('Valores')
    plt.title(f'Solución del Sistema de Ecuaciones\nSolucion: {x}\nIterciones: {i}')
    plt.grid(True)
    plt.show()

def capturar_parametros_gauss_seidel(A, b, x0_str, tol_str, max_iter_str):
    try:
        x0 = [float(num) for num in x0_str.split(",")]
        tol = float(tol_str)
        max_iter = int(max_iter_str)
        x, iteraciones = gauss_seidel(A, b, x0, tol, max_iter)
        
        return A, b, x, iteraciones
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def generate_matrix_entries(size_entry, matrix_frame, matrix_entries):
    for widget in matrix_frame.winfo_children():
        widget.destroy()

    matrix_entries.clear()

    try:
        n = int(size_entry.get())
        for i in range(n):
            row_entries = []
            for j in range(n):
                entry = tk.Entry(matrix_frame, width=5)
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, "0") 
                row_entries.append(entry)
            matrix_entries.append(row_entries)
    except ValueError:
        messagebox.showerror("Error", "El tamaño de la matriz debe ser un número entero")

def collect_matrix(matrix_entries):
    try:
        matrix = []
        for row_entries in matrix_entries:
            row = [float(entry.get()) for entry in row_entries]
            matrix.append(row)
        return np.array(matrix)
    except ValueError:
        messagebox.showerror("Error", "Todos los elementos de la matriz deben ser números válidos")
        return None

def collect_vector(vector_entries):
    try:
        return np.array([float(entry.get()) for entry in vector_entries])
    except ValueError:
        messagebox.showerror("Error", "Todos los elementos del vector deben ser números válidos")
        return None

def interfaz_grafica_gauss():
    root = tk.Tk()
    root.title("Método de Gauss-Seidel")
    window_width = 800
    window_height = 430
    root.resizable(False, False)
    root.geometry(f"{window_width}x{window_height}")
    root.configure(bg="#f0f0f0")
    center_window(root, window_width, window_height)

    frame_izquierdo = tk.Frame(root, bg="#f0f0f0")
    frame_izquierdo.pack(side=tk.LEFT, padx=20, pady=10)
    frame_derecho = tk.Frame(root, bg="#f0f0f0")
    frame_derecho.pack(side=tk.RIGHT, padx=20, pady=20)

    tk.Label(frame_izquierdo, text="Tamaño de la matriz (n x n):", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
    size_entry = tk.Entry(frame_izquierdo, width=5)
    size_entry.grid(row=0, column=1, padx=10, pady=10)
    size_entry.insert(0, "3")

    matrix_frame = tk.Frame(frame_izquierdo, bg="#f0f0f0")
    matrix_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    matrix_entries = []

    vector_frame = tk.Frame(frame_izquierdo, bg="#f0f0f0")
    vector_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    vector_entries = []

    def generate_matrix_and_vector():
        generate_matrix_entries(size_entry, matrix_frame, matrix_entries)

        for widget in vector_frame.winfo_children():
            widget.destroy()

        vector_entries.clear()

        n = int(size_entry.get())
        for i in range(n):
            entry = tk.Entry(vector_frame, width=5)
            entry.grid(row=i, column=0, padx=2, pady=2)
            entry.insert(0, "0") 
            vector_entries.append(entry)

    generate_button = tk.Button(frame_izquierdo, text="Generar matriz y vector", command=generate_matrix_and_vector, bg="#4CAF50", fg="white")
    generate_button.grid(row=0, column=2, padx=10, pady=10)

    tk.Label(frame_derecho, text="Condiciones iniciales y parámetros:", bg="#f0f0f0").grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    tk.Label(frame_derecho, text="Vector inicial (x0):", bg="#f0f0f0").grid(row=1, column=0)
    x0_entry = tk.Entry(frame_derecho, width=30)
    x0_entry.grid(row=1, column=1, padx=10, pady=10)
    x0_entry.insert(0, "0,0,0")

    tk.Label(frame_derecho, text="Tolerancia:", bg="#f0f0f0").grid(row=2, column=0)
    tol_entry = tk.Entry(frame_derecho, width=10)
    tol_entry.grid(row=2, column=1, padx=10, pady=10)
    tol_entry.insert(0, "0.0001")

    tk.Label(frame_derecho, text="Iteraciones máximas:", bg="#f0f0f0").grid(row=3, column=0)
    max_iter_entry = tk.Entry(frame_derecho, width=10)
    max_iter_entry.grid(row=3, column=1, padx=10, pady=10)
    max_iter_entry.insert(0, "100")   

    def on_calculate():
        A = collect_matrix(matrix_entries)
        b = collect_vector(vector_entries)
        if A is None or b is None:
            return

        try:
            x0_str = x0_entry.get()
            tol_str = tol_entry.get()
            max_iter_str = max_iter_entry.get()
            root.destroy()
            A, b, x, i =capturar_parametros_gauss_seidel(A, b, x0_str, tol_str, max_iter_str)
            plot_solution(A, b, x, i)
        except ValueError:
            messagebox.showerror("Error", "Los valores iniciales y los parámetros deben ser números válidos")

    calculate_button = tk.Button(frame_derecho, text="Calcular", command=on_calculate, bg="#4CAF50", fg="white")
    calculate_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    interfaz_grafica_gauss()
