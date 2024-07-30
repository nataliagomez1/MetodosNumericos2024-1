import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from GUI.calculadora import teclado, center_window, validate_entry_ecu, validate_entry_decInt
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

def capturar_parametros_biseccion(func_str, a, b, tol, ventana):
    try:
        func_str = func_str.replace("√", "sqrt")
        func_str = func_str.replace("e", "2.7182818284")
        x = sp.symbols('x')
        f = sp.sympify(func_str)
        func = sp.lambdify(x, f, 'numpy')
        
        a = float(a)
        b = float(b)
        tol = float(tol)
        raiz = biseccion(func, a, b, tol)
        if raiz is not None:
            ventana.destroy()  
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
    ventana = tk.Tk()
    ventana.title("Método de Bisección")
    window_width = 800
    window_height = 430
    ventana.resizable(False, False)

    ventana.geometry(f"{window_width}x{window_height}")
    center_window(ventana, window_width, window_height)

    frame_izquierdo = tk.Frame(ventana, bg="#f0f0f0")
    frame_izquierdo.pack(side=tk.LEFT, padx=20, pady=20)

    frame_derecho = tk.Frame(ventana, bg="#f0f0f0")
    frame_derecho.pack(side=tk.RIGHT, padx=20, pady=20)

    etiqueta_func = tk.Label(frame_izquierdo, text="Ingrese la función f(x):", bg="#f0f0f0")
    etiqueta_func.grid(row=0, column=0, padx=10, pady=10)

    vcmd_func = (ventana.register(validate_entry_ecu), '%P')
    entrada_func = tk.Entry(frame_izquierdo, width=40, validate='key', validatecommand=vcmd_func)
    entrada_func.grid(row=1, column=0, padx=10, pady=10)
    
    etiqueta_a = tk.Label(frame_izquierdo, text="Valor de a:", bg="#f0f0f0")
    etiqueta_a.grid(row=2, column=0, padx=10, pady=10)

    vcmd_a = (ventana.register(validate_entry_decInt), '%P')
    entrada_a = tk.Entry(frame_izquierdo, width=40, validate='key', validatecommand=vcmd_a)
    entrada_a.grid(row=3, column=0, padx=10, pady=10)

    etiqueta_b = tk.Label(frame_izquierdo, text="Valor de b:", bg="#f0f0f0")
    etiqueta_b.grid(row=4, column=0, padx=10, pady=10)

    vcmd_b = (ventana.register(validate_entry_decInt), '%P')
    entrada_b = tk.Entry(frame_izquierdo, width=40, validate='key', validatecommand=vcmd_b)
    entrada_b.grid(row=5, column=0, padx=10, pady=10)

    etiqueta_tol = tk.Label(frame_izquierdo, text="Tolerancia:", bg="#f0f0f0")
    etiqueta_tol.grid(row=6, column=0, padx=10, pady=10)

    vcmd_tol = (ventana.register(validate_entry_decInt), '%P')
    entrada_tol = tk.Entry(frame_izquierdo, width=40, validate='key', validatecommand=vcmd_tol)
    entrada_tol.grid(row=7, column=0, padx=10, pady=10)

    teclado(frame_derecho, entrada_func)
    
    def ejecutar_biseccion():
        func_str = entrada_func.get()
        a = entrada_a.get()
        b = entrada_b.get()
        tol = entrada_tol.get()
        capturar_parametros_biseccion(func_str, a, b, tol, ventana)

    boton_ejecutar = tk.Button(frame_izquierdo, text="Ejecutar", command=ejecutar_biseccion, bg="#4CAF50", fg="white")
    boton_ejecutar.grid(row=8, column=0, padx=10, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    interfaz_grafica_biseccion()



