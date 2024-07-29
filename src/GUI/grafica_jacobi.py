import tkinter as tk
from tkinter import messagebox
from methods.jacobi import generate_matrix_entries, collect_matrix, calculate_jacobi, collect_vector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar_jacobi():
    root = tk.Tk()
    root.title("Método de Jacobi")
    root.geometry("800x600")
    root.configure(bg="#f0f0f0")

    tk.Label(root, text="Tamaño de la matriz (n x n):").grid(row=0, column=0, padx=10, pady=10)
    size_entry = tk.Entry(root, width=5)
    size_entry.grid(row=0, column=1, padx=10, pady=10)
    size_entry.insert(0, "3")  # Tamaño predeterminado

    matrix_frame = tk.Frame(root)
    matrix_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    matrix_entries = []

    vector_frame = tk.Frame(root)
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
            entry.insert(0, "0")  # Prellenar con ceros
            vector_entries.append(entry)

    generate_button = tk.Button(root, text="Generar matriz y vector", command=generate_matrix_and_vector, bg="#4CAF50", fg="white")
    generate_button.grid(row=0, column=2, padx=10, pady=10)

    tk.Label(root, text="Condiciones iniciales y parámetros:").grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    tk.Label(root, text="Vector inicial (x0):").grid(row=4, column=0)
    x0_entry = tk.Entry(root, width=30)
    x0_entry.grid(row=4, column=1, padx=10, pady=10)
    x0_entry.insert(0, "0,0,0")

    tk.Label(root, text="Tolerancia:").grid(row=5, column=0)
    tol_entry = tk.Entry(root, width=10)
    tol_entry.grid(row=5, column=1, padx=10, pady=10)
    tol_entry.insert(0, "0.0001")

    tk.Label(root, text="Iteraciones máximas:").grid(row=6, column=0)
    max_iter_entry = tk.Entry(root, width=10)
    max_iter_entry.grid(row=6, column=1, padx=10, pady=10)
    max_iter_entry.insert(0, "100")

    def show_results_window(result, iterations, errors):
        result_window = tk.Toplevel(root)
        result_window.title("Resultados del Método de Jacobi")
        result_window.geometry("800x600")
        result_window.configure(bg="#f0f0f0")
        
        result_label = tk.Label(result_window, text=f"Solución: {result}\nIteraciones: {iterations}", bg="#f0f0f0")
        result_label.pack(pady=10)
        
        fig, ax = plt.subplots()
        ax.plot(errors, label='Error')
        ax.set_xlabel('Iteración')
        ax.set_ylabel('Error')
        ax.set_title('Convergencia del Método de Jacobi')
        ax.legend()
        
        canvas = FigureCanvasTkAgg(fig, master=result_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def on_calculate():
        A = collect_matrix(matrix_entries)
        b = collect_vector(vector_entries)
        if A is None or b is None:
            return

        try:
            x0 = [float(num) for num in x0_entry.get().split(",")]
            tol = float(tol_entry.get())
            max_iterations = int(max_iter_entry.get())
            result, iterations, errors = calculate_jacobi(A, b, x0, tol, max_iterations)
            show_results_window(result, iterations, errors)
        except ValueError:
            messagebox.showerror("Error", "Los valores iniciales y los parámetros deben ser números válidos")

    calculate_button = tk.Button(root, text="Calcular", command=on_calculate, bg="#4CAF50", fg="white")
    calculate_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    graficar_jacobi()

