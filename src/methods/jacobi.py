import numpy as np
import tkinter as tk
from tkinter import messagebox

def generate_matrix_entries(size_entry, matrix_frame, matrix_entries):
    try:
        n = int(size_entry.get())
        if n <= 0:
            raise ValueError("El tamaño debe ser un entero positivo")
        
        for widget in matrix_frame.winfo_children():
            widget.destroy()
        
        matrix_entries.clear()
        
        for i in range(n):
            row_entries = []
            for j in range(n):
                entry = tk.Entry(matrix_frame, width=5)
                entry.grid(row=i, column=j, padx=2, pady=2)
                entry.insert(0, "0")  # Prellenar con ceros
                row_entries.append(entry)
            matrix_entries.append(row_entries)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def collect_matrix(matrix_entries):
    try:
        n = len(matrix_entries)
        A = []
        for row_entries in matrix_entries:
            row = []
            for entry in row_entries:
                value = float(entry.get())
                row.append(value)
            A.append(row)
        return A
    except ValueError:
        messagebox.showerror("Error", "Todos los valores deben ser números.")
        return None

def collect_vector(vector_entries):
    try:
        b = [float(entry.get()) for entry in vector_entries]
        return b
    except ValueError:
        messagebox.showerror("Error", "Todos los valores del vector deben ser números.")
        return None

def calculate_jacobi(A, b, x0, tol, max_iterations):
    n = len(A)
    x = x0[:]
    errors = []
    for k in range(max_iterations):
        x_new = x[:]
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x_new[i] = (b[i] - s) / A[i][i]
        error = np.linalg.norm(np.array(x_new) - np.array(x))
        errors.append(error)
        if error < tol:
            return x_new, k + 1, errors
        x = x_new
    return x, max_iterations, errors
