import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, Frame, messagebox
from methods.gaussseidel import gauss_seidel

def plot_solution(A, b, x):
    n = len(b)
    x_vals = np.arange(1, n + 1)
    y_vals = x

    plt.figure(figsize=(10, 6))
    plt.bar(x_vals, y_vals, align='center')
    plt.xticks(x_vals, [f'x{i+1}' for i in range(n)])
    plt.xlabel('Variables')
    plt.ylabel('Valores')
    plt.title('Solución del Sistema de Ecuaciones')
    plt.grid(True)
    plt.show()

def capturar_parametros_gauss_seidel(A_str, b_str, x0_str, tol_str, max_iter_str):
    try:
        A = np.array(eval(A_str))
        b = np.array(eval(b_str))
        x0 = np.array(eval(x0_str))
        tol = float(tol_str)
        max_iter = int(max_iter_str)
        
        x, iteraciones = gauss_seidel(A, b, x0, tol, max_iter)
        
        messagebox.showinfo("Resultado", f"Solución: {x}\nIteraciones: {iteraciones}")
        plot_solution(A, b, x)
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

def interfaz_grafica_gauss_seidel():
    root = Tk()
    root.title("Método de Gauss-Seidel")

    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    Label(frame, text="Matriz A:").grid(row=0, column=0)
    global entry_A
    entry_A = StringVar()
    Entry(frame, textvariable=entry_A).grid(row=0, column=1)

    Label(frame, text="Vector b:").grid(row=1, column=0)
    global entry_b
    entry_b = StringVar()
    Entry(frame, textvariable=entry_b).grid(row=1, column=1)

    Label(frame, text="Vector x0:").grid(row=2, column=0)
    global entry_x0
    entry_x0 = StringVar()
    Entry(frame, textvariable=entry_x0).grid(row=2, column=1)

    Label(frame, text="Tolerancia:").grid(row=3, column=0)
    global entry_tol
    entry_tol = StringVar()
    Entry(frame, textvariable=entry_tol).grid(row=3, column=1)

    Label(frame, text="Máx. Iteraciones:").grid(row=4, column=0)
    global entry_max_iter
    entry_max_iter = StringVar()
    Entry(frame, textvariable=entry_max_iter).grid(row=4, column=1)

    def ejecutar_gauss_seidel():
        A_str = entry_A.get()
        b_str = entry_b.get()
        x0_str = entry_x0.get()
        tol_str = entry_tol.get()
        max_iter_str = entry_max_iter.get()
        capturar_parametros_gauss_seidel(A_str, b_str, x0_str, tol_str, max_iter_str)

    Button(frame, text="Ejecutar", command=ejecutar_gauss_seidel).grid(row=5, column=0, columnspan=2)

    root.mainloop()
