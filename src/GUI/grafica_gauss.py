import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, Frame, messagebox

from utils.funcionesaux import verificar_y_despejar_ecuaciones
from methods.gaussseidel import gauss_seidel

def graficar_ecuaciones(ecuaciones, variables):
    fig, ax = plt.subplots()
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    for eq in ecuaciones:
        Z = sp.lambdify(variables, eq, 'numpy')
        ax.contour(X, Y, Z(X, Y), levels=[0])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()

def capturar_parametros_gauss_seidel(ecuaciones, tol, max_iter):
    variables = sp.symbols(f'x1:{len(ecuaciones)+1}')
    despejadas = verificar_y_despejar_ecuaciones(ecuaciones, variables)
    if despejadas is None:
        return None, None, None, None, None, "Hubo un error en el despeje de las ecuaciones. Por favor, verifica las ecuaciones ingresadas."

    A = []
    b = []
    for eq in ecuaciones:
        coeficientes = [eq.coeff(var) for var in variables] + [eq.as_coeff_add()[0]]
        A.append(coeficientes[:-1])
        b.append(-coeficientes[-1])
    x0 = np.zeros(len(A))
    
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    sol, iters = gauss_seidel(A, b, x0, tol, max_iter)
    
    graficar_ecuaciones(ecuaciones, variables)
    
    return A, b, x0, tol, max_iter, f'Solución: {sol}\nIteraciones: {iters}'

def interfaz_grafica_gauss():
    root = Tk()
    root.title("Método de Gauss-Seidel")

    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    Label(frame, text="Número de ecuaciones:").grid(row=0, column=0)
    num_ecuaciones = StringVar()
    Entry(frame, textvariable=num_ecuaciones).grid(row=0, column=1)

    def crear_campos_ecuaciones():
        try:
            n = int(num_ecuaciones.get())
            if n <= 0:
                raise ValueError("El número de ecuaciones debe ser positivo.")
            
            global ecuacion_entries
            ecuacion_entries = []
            for i in range(n):
                Label(frame, text=f"Ecuación {i+1}:").grid(row=i+1, column=0)
                entry = Entry(frame)
                entry.grid(row=i+1, column=1, columnspan=4, sticky="ew")
                ecuacion_entries.append(entry)
            
            Label(frame, text="Tolerancia:").grid(row=n+1, column=0)
            global tolerancia
            tolerancia = StringVar()
            Entry(frame, textvariable=tolerancia).grid(row=n+1, column=1)
            
            Label(frame, text="Iteraciones:").grid(row=n+2, column=0)
            global iteraciones
            iteraciones = StringVar()
            Entry(frame, textvariable=iteraciones).grid(row=n+2, column=1)
            
            Button(frame, text="Ejecutar", command=ejecutar_gauss_seidel).grid(row=n+3, column=0, columnspan=5)

            global resultado
            resultado = StringVar()
            Label(frame, textvariable=resultado).grid(row=n+4, column=0, columnspan=5)

        except ValueError as e:
            messagebox.showerror("Error", f"Error: {e}")

    def ejecutar_gauss_seidel():
        ecuaciones = [sp.sympify(entry.get()) for entry in ecuacion_entries]
        try:
            tol = float(tolerancia.get())
            if tol <= 0:
                messagebox.showerror("Error", "La tolerancia debe ser un número positivo.")
                return
            max_iter = int(iteraciones.get())
            if max_iter <= 0:
                messagebox.showerror("Error", "El número máximo de iteraciones debe ser un entero positivo.")
                return

            A, b, x0, tol, max_iter, resultado_texto = capturar_parametros_gauss_seidel(ecuaciones, tol, max_iter)
            if A is None:
                messagebox.showerror("Error", resultado_texto)
            else:
                resultado.set(resultado_texto)
        except ValueError as e:
            messagebox.showerror("Error", f"Error en los parámetros de tolerancia o número de iteraciones: {e}")

    Button(frame, text="Crear Campos", command=crear_campos_ecuaciones).grid(row=1, column=0, columnspan=2)

    root.mainloop()