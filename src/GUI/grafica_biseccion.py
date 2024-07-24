import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, Frame, messagebox

from methods.biseccion import biseccion  

def plot_graph(func, a, b, raiz):
    x = sp.symbols('x')
    expr = sp.sympify(func)
    f = sp.lambdify(x, expr, 'numpy')

    x_vals = np.linspace(a, b, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {func}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.scatter([raiz], [f(raiz)], color='red')
    plt.title('Método de Bisección')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def capturar_parametros_biseccion(func_str, a, b, tol):
    try:
        x = sp.symbols('x')
        f = sp.sympify(func_str)
        func = sp.lambdify(x, f, 'numpy')
        
        a = float(a)
        b = float(b)
        tol = float(tol)
        raiz = biseccion(func, a, b, tol)
        if raiz is not None:
            plot_graph(func_str, a, b, raiz)
        else:
            messagebox.showinfo("Resultado", "No se encontró raíz en el intervalo dado.")
        
    except sp.SympifyError:
        messagebox.showerror("Error", "La función ingresada no es válida. Por favor, verifica la sintaxis.")
    except ValueError:
        messagebox.showerror("Error", "Los valores de a, b y tol deben ser numéricos.")
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

def interfaz_grafica_biseccion():
    root = Tk()
    root.title("Método de Bisección")
    root.geometry("400x300")

    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    Label(frame, text="Función f(x):").grid(row=0, column=0)
    global entry_func
    entry_func = StringVar()
    Entry(frame, textvariable=entry_func).grid(row=0, column=1)

    Label(frame, text="Valor de a:").grid(row=1, column=0)
    global entry_a
    entry_a = StringVar()
    Entry(frame, textvariable=entry_a).grid(row=1, column=1)

    Label(frame, text="Valor de b:").grid(row=2, column=0)
    global entry_b
    entry_b = StringVar()
    Entry(frame, textvariable=entry_b).grid(row=2, column=1)

    Label(frame, text="Tolerancia:").grid(row=3, column=0)
    global entry_tol
    entry_tol = StringVar()
    Entry(frame, textvariable=entry_tol).grid(row=3, column=1)

    def ejecutar_biseccion():
        func_str = entry_func.get()
        a = entry_a.get()
        b = entry_b.get()
        tol = entry_tol.get()
        capturar_parametros_biseccion(func_str, a, b, tol)

    Button(frame, text="Ejecutar", command=ejecutar_biseccion).grid(row=4, column=0, columnspan=2)

    root.mainloop()



