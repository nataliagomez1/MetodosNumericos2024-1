import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import GUI.grafica_trapecio as trapecio
import GUI.grafica_puntofijo as punto_fijo
import GUI.grafica_newton as newton
import GUI.grafica_secante as secante
import GUI.grafica_gauss as gauss
import GUI.grafica_jacobi as jacobi

# Nombres de los botones e imágenes
button_names = ['Punto fijo', 'Biseccion', 'New Raphson', 'Secante', 'Jacobi', 
                'Gauss-Seidel', 'Simpon', 'Trapecio', 'Euler', 'Expo']

# Rutas de las imágenes
image_paths = [f'./Recursos/image{i}.png' for i in range(1, 11)]

def on_button_click(button_name):
    if(button_name == 'Trapecio'):
        trapecio.auxTrapecio()
    elif(button_name == 'Punto fijo'):
        punto_fijo.graficar_ecuacion_punto_fijo() 
    elif(button_name == 'Biseccion'):
        punto_fijo.graficar_ecuacion_punto_fijo() #FALTA
    elif(button_name == 'New Raphson'):
        newton.graficar_ecuacion()
    elif(button_name == 'Secante'):
        secante.graficar_ecuacion()
    elif(button_name == 'Jacobi'):
        jacobi.graficar_jacobi()
    elif(button_name == 'Gauss-Seidel'):
        gauss.interfaz_grafica_gauss()
    elif(button_name == 'Simpon'):
        punto_fijo.graficar_ecuacion_punto_fijo() #FALTA
    elif(button_name == 'Euler'):
        punto_fijo.graficar_ecuacion_punto_fijo() #FALTA
    elif(button_name == 'Expo'):
        punto_fijo.graficar_ecuacion_punto_fijo() #FALTA

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
            image = image.resize((120, 120), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            button = ttk.Button(frame, text=button_names[index], image=photo, compound='top',
                                command=lambda name=button_names[index]: on_button_click(name))
            button.image = photo
            button.pack(expand=True, fill='both')
