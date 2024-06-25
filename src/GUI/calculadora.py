import tkinter as tk

def button_action(button_number):
    print(f"Button {button_number} clicked: Action {button_number}")
    if button_number == 1:
        create_calculator()

def button_action_calc(button_text, text_var, entry):
    print(f"Button {button_text} clicked: Action {button_text}")
    current_text = text_var.get()
    if button_text == "borrar":
        new_text = current_text[:-1]
    elif button_text == "clear":
        new_text = ""
    else:
        new_text = current_text + button_text
    text_var.set(new_text)
    entry.delete(0, tk.END)
    entry.insert(0, new_text)
    print(f"Updated text: {new_text}")  

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")

def create_calculator():
    root = tk.Tk()
    root.title("INGRESAR ECUACIÓN")
    root.resizable(width=False, height=False)
    
    text_var = tk.StringVar()

    window_width = 780
    window_height = 530
    root.geometry(f"{window_width}x{window_height}")
    center_window(root, window_width, window_height)
    
    entry = tk.Entry(root, textvariable=text_var, font=("Arial", 18))
    entry.grid(row=0, column=0, columnspan=6)
    
    button_texts = [
        "+", "-", "*", "/", "^", "√",
        "(", ")", ".", "=", "x", "e",
        "1", "2", "3", "4", "5", "6",
        "7", "8", "9", "0", "borrar", "clear"
    ]
    
    for i, texto in enumerate(button_texts, start=1):
        button = tk.Button(
            root, text=texto,
            command=lambda t=texto: button_action_calc(t, text_var, entry),
            bg="lightblue", fg="darkblue", 
            activebackground="blue", activeforeground="white",  
            width=5, height=2, padx=10, pady=5
        )
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
    center_window(root, window_width, window_height)

    method_texts = [
        "Punto fijo", "Biseccion", "Newton - Raphson", "Secante", 
        "Jacobi", "Gauss - Seidel", "7", "8", "9", "10"
    ]
    
    for i, texto in enumerate(method_texts, start=1):
        button = tk.Button(
            root, text=texto,
            command=lambda i=i: button_action(i),
            bg="lightblue", fg="darkblue", 
            activebackground="blue", activeforeground="white",  
            width=50, height=5, padx=10, pady=5
        )
        row = (i - 1) // 2
        column = (i - 1) % 2
        button.grid(row=row, column=column, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
