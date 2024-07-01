import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import methods.trapecio as trapecio

def graficar_trapecio(f, a, b, n, result):
    x = np.linspace(a, b, 1000)
    y = f(x)
    
    plt.plot(x, y, label='f(x)')
    
    h = (b - a) / n
    x_trapecios = np.linspace(a, b, n + 1)
    y_trapecios = f(x_trapecios)
    
    for i in range(n):
        plt.fill([x_trapecios[i], x_trapecios[i], x_trapecios[i+1], x_trapecios[i+1]], 
                 [0, y_trapecios[i], y_trapecios[i+1], 0], 'b', edgecolor='r', alpha=0.2)
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title(f'Método del Trapecio\nIntegral aproximada= {result}')
    
    plt.grid(True)
    plt.show()

def auxTrapecio():
    def str_to_func(func_str):
        try:
            code = compile("f = lambda x: " + func_str, "<string>", "exec")
            scope = {}
            exec(code, {}, scope)
            return scope['f']
        except Exception as e:
            messagebox.showerror("Error", f"Error en la función: {e}")
            return None

    def calculate_trapecio():
        try:
            func_str = entry_func.get()
            f = str_to_func(func_str)
            if f is None:
                return
            a = float(entry_a.get())
            b = float(entry_b.get())
            n = int(entry_n.get())
            if a >= b:
                messagebox.showerror("Error", "El valor de 'a' debe ser menor que 'b'.")
                return
            if n <= 0:
                messagebox.showerror("Error", "El número de trapecios debe ser mayor que 0.")
                return
            result = trapecio.trapecio(f, a, b, n)
            #messagebox.showinfo("Resultado", f"La integral aproximada es: {result}")
            graficar_trapecio(f, a, b, n, result)
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos.")

    app = tk.Tk()
    app.title("Método del Trapecio")

    tk.Label(app, text="Función (en términos de x):").grid(row=0, column=0)
    entry_func = tk.Entry(app)
    entry_func.grid(row=0, column=1)

    tk.Label(app, text="Inicio del intervalo (a):").grid(row=1, column=0)
    entry_a = tk.Entry(app)
    entry_a.grid(row=1, column=1)

    tk.Label(app, text="Fin del intervalo (b):").grid(row=2, column=0)
    entry_b = tk.Entry(app)
    entry_b.grid(row=2, column=1)

    tk.Label(app, text="Número de trapecios (n):").grid(row=3, column=0)
    entry_n = tk.Entry(app)
    entry_n.grid(row=3, column=1)

    calculate_button = tk.Button(app, text="Calcular", command=calculate_trapecio)
    calculate_button.grid(row=4, columnspan=2)

    app.mainloop()

