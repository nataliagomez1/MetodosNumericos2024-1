import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Nombres de los botones e imágenes
button_names = ['Punto fijo', 'Biseccion', 'New Raphson', 'Secante', 'Jacobi', 
                'Gauss-Seidel', 'Simpomp', 'Trapezio', 'Euler', 'Expo']

# Rutas de las imágenes
image_paths = [f'image.png' for i in range(1, 11)]

def on_button_click(button_name):
    print(f'{button_name} clicked')

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu with Buttons")
        self.geometry("800x400")
        self.create_widgets()

    def create_widgets(self):
        # Añadir el título
        title_label = ttk.Label(self, text="Métodos Numéricos", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=5, pady=10)

        # Configurar la cuadrícula
        for i in range(1, 3): # 3 filas incluyendo el título
            self.grid_rowconfigure(i, weight=1)
        for j in range(5): # 5 columnas
            self.grid_columnconfigure(j, weight=1)

        for index in range(10):
            row = (index // 5) + 1  # Ajustar filas para dejar espacio al título
            col = index % 5

            frame = ttk.Frame(self)
            frame.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')

            image = Image.open(image_paths[index])
            image = image.resize((50, 50), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            button = ttk.Button(frame, text=button_names[index], image=photo, compound='top',
                                command=lambda name=button_names[index]: on_button_click(name))
            button.image = photo
            button.pack(expand=True, fill='both')
