import tkinter as tk

def button_action(button_number):
    print(f"Button {button_number} clicked: Action {button_number}")
    if(button_number==1):
        create_calculator()





def button_action_calc(button_text,text_var):
    print(f"Button {button_text} clicked: Action {button_text}")
    if(button_text=="+"):
        current_text = text_var.get
        text_var.set(current_text + button_text)
        

def center_window(window, width, height):
    # Obtener dimensiones de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Establecer la posición de la ventana
    window.geometry(f"{width}x{height}+{x}+{y}")
def create_calculator():
    root = tk.Tk()
    root.title("INGRESAR ECUACIÓN")
    root.resizable(width=False, height=False)
    # Variable para almacenar el texto ingresado
    text_var = tk.StringVar()

    window_width = 780
    window_height = 530
    root.geometry(f"{window_width}x{window_height}")
    center_window(root, window_width, window_height)
    
    # Crear la caja de texto
    entry = tk.Entry(root, textvariable=text_var, font=("Arial", 18))
    entry.grid(row=0, column=0, columnspan=10)
    
    for i in range(1, 25):
        if(i==1):
            texto="+"
        elif(i==2):
            texto="-"
        elif(i==3):
            texto="*"
        elif(i==4):
            texto="/"
        elif(i==5):
            texto="^"
        elif(i==6):
            texto="√"
        elif(i==7):
            texto="("
        elif(i==8):
            texto=")"
        elif(i==9):
            texto="."
        elif(i==10):
            texto="="
        elif(i==11):
            texto="x"
        elif(i==12):
            texto="e"
        elif(i==13):
            texto="1"
        elif(i==14):
            texto="2"
        elif(i==15):
            texto="3"
        elif(i==16):
            texto="4"
        elif(i==17):
            texto="5"
        elif(i==18):
            texto="6"
        elif(i==19):
            texto="7"
        elif(i==20):
            texto="8"
        elif(i==21):
            texto="9"
        elif(i==22):
            texto="0"
        elif(i==23):
            texto="borrar"
        elif(i==24):
            texto="clear"
            
        if(texto=="+"):
            button = tk.Button(root, 
                            text=texto,
                            command=lambda i=i: button_action_calc(i,text_var),
                            bg="lightblue", fg="darkblue", activebackground="blue", activeforeground="white",  
                            width=2, height=2, padx=10, pady=5)
        else:
            button = tk.Button(root, 
                            text=texto,
                            bg="lightblue", fg="darkblue", activebackground="blue", activeforeground="white",  
                            width=2, height=2, padx=10, pady=5)
        row = (i - 1) // 6
        column = (i - 1) % 6
        button.grid(row=row+1, column=column, padx=5, pady=5)

    root.mainloop()



def create_gui():
    root = tk.Tk()
    root.title("CALCULADORA DE MÉTODOS NUMÉRICOS")
    root.resizable(width=False, height=False)

    window_width = 780
    window_height = 530
    root.geometry(f"{window_width}x{window_height}")

    # Llamar función para centrar la ventana
    center_window(root, window_width, window_height)

    for i in range(1, 11):
        if(i==1):
            texto="Punto fijo"
        elif(i==2):
            texto="Biseccion"
        elif(i==3):
            texto="Newton - Raphson"
        elif(i==4):
            texto="Secante"
        elif(i==5):
            texto="Jacobi"
        elif(i==6):
            texto="Gauss - Seidel"
        elif(i==7):
            texto="7"
        elif(i==8):
            texto="8"
        elif(i==9):
            texto="9"
        elif(i==10):
            texto="10"
            
        button = tk.Button(root, text=texto,
                           command=lambda i=i: button_action(i),
                           bg="lightblue",     
                           fg="darkblue",      
                           activebackground="blue",  
                           activeforeground="white",  
                           width=50,           
                           height=5,           
                           padx=10,            
                           pady=5)
        # Calculate row and column index
        row = (i - 1) // 2
        column = (i - 1) % 2
        button.grid(row=row, column=column, padx=5, pady=5)

    root.mainloop()



if __name__ == "__main__":
    create_gui()
    # create_calculator()
