import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import methods.trapecio as trapecio
from GUI.calculadora import center_window, teclado, teclado_digitos

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
            ecuacion = entrada_ecuacion.get()
            ecuacion = ecuacion.replace("√", "sqrt")
            ecuacion = ecuacion.replace("e", "2.7182818284")
            ecuacion = ecuacion.replace("^", "**")
        
            func_str = str(ecuacion)
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
    window_width = 580
    window_height = 630
    app.geometry(f"{window_width}x{window_height}")
    center_window(app, window_width, window_height)

    app.configure(bg="#f0f0f0")
    
    etiqueta = tk.Label(app, text="Ingrese la ecuación en términos de x:", bg="#f0f0f0")
    etiqueta.grid(row=0, column=2, columnspan=6)

    def validate_entry_ecu(new_value):
        allowed_chars = "0123456789x√().+-*/^e"
        for char in new_value:
            if char not in allowed_chars:
                return False
        return True

    vcmdecu = (app.register(validate_entry_ecu), '%P')
    entrada_ecuacion = tk.Entry(app, width=40, validate='key', validatecommand=vcmdecu)
    entrada_ecuacion.grid(row=1, column=2, columnspan=6)
    
    teclado(app,entrada_ecuacion)

    tk.Label(app, text="Limite inferior (a):").grid(row=8, column=2, columnspan=6)
    entry_a = tk.Entry(app)
    entry_a.grid(row=9, column=2, columnspan=6)

    tk.Label(app, text="Limite superior (b):").grid(row=10, column=2, columnspan=6)
    entry_b = tk.Entry(app)
    entry_b.grid(row=11, column=2, columnspan=6)

    tk.Label(app, text="Número de trapecios (n):").grid(row=12, column=2, columnspan=6)
    entry_n = tk.Entry(app)
    entry_n.grid(row=13, column=2, columnspan=6)

    calculate_button = tk.Button(app, text="Calcular", command=calculate_trapecio)
    calculate_button.grid(row=15, columnspan=6, column=2)

    app.mainloop()
