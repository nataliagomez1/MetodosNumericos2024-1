import tkinter as tk
from tkinter import messagebox
import numpy as np
import methods.jacobi as jacobi

def graficar_jacobi():
    def calculate_jacobi():
        try:
            A = eval(entry_A.get())
            b = eval(entry_b.get())
            x0 = eval(entry_x0.get())
            tol = float(entry_tol.get())
            max_iter = int(entry_max_iter.get())
            A = np.array(A, dtype=float)
            b = np.array(b, dtype=float)
            x0 = np.array(x0, dtype=float)
            if A.shape[0] != A.shape[1]:
                messagebox.showerror("Error", "La matriz A debe ser cuadrada.")
                return
            if A.shape[0] != b.shape[0] or A.shape[0] != x0.shape[0]:
                messagebox.showerror("Error", "Las dimensiones de A, b y x0 no coinciden.")
                return
            solution = jacobi.jacobi_method(A, b, x0, tol, max_iter)
            messagebox.showinfo("Resultado", f"Solución: {solution}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    app = tk.Tk()
    app.title("Método de Jacobi")

    tk.Label(app, text="Matriz A:").grid(row=0, column=0)
    entry_A = tk.Entry(app)
    entry_A.grid(row=0, column=1)

    tk.Label(app, text="Vector b:").grid(row=1, column=0)
    entry_b = tk.Entry(app)
    entry_b.grid(row=1, column=1)

    tk.Label(app, text="Vector x0:").grid(row=2, column=0)
    entry_x0 = tk.Entry(app)
    entry_x0.grid(row=2, column=1)

    tk.Label(app, text="Tolerancia:").grid(row=3, column=0)
    entry_tol = tk.Entry(app)
    entry_tol.grid(row=3, column=1)

    tk.Label(app, text="Máximo de iteraciones:").grid(row=4, column=0)
    entry_max_iter = tk.Entry(app)
    entry_max_iter.grid(row=4, column=1)

    calculate_button = tk.Button(app, text="Calcular", command=calculate_jacobi)
    calculate_button.grid(row=5, columnspan=2)

    app.mainloop()
