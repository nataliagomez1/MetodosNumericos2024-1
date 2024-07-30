import tkinter as tk
def button_action_calc(button_text, text_var, entry):
    print(f"Button {button_text} clicked: Action {button_text}")
    current_text = text_var.get()
    if button_text == "borrar":
        new_text = current_text[:-1]
    elif button_text == "clear":
        new_text = ""
    elif button_text== "xⁿ":
        new_text= current_text+"^"
    elif button_text== "√":
        new_text=current_text+"sqrt"
    elif button_text== "e":
        new_text=current_text+"2.718281"
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

def teclado(root,entry):
    text_var = tk.StringVar()
    button_texts = [
        "7", "8", "9", "/", "x\u207f", "√",
        "4", "5", "6", "=", "x", "e",
        "1", "2", "3", "+", "-", "*",
        "0", ".", "(", ")", "borrar", "clear",
        "sin(", "cos("
    ]
    
    for i, texto in enumerate(button_texts, start=1):
        if texto.isdigit():
            button = tk.Button(
            root, text=texto,
            command=lambda t=texto: button_action_calc(t, text_var, entry),
            bg="#464158", fg="white", 
            activebackground="#9E7682", activeforeground="white",  
            width=5, height=2, padx=5, pady=5,font=("Arial",12)
            )
        else:
            button = tk.Button(
            root, text=texto,
            command=lambda t=texto: button_action_calc(t, text_var, entry),
            bg="#605770", fg="white", 
            activebackground="#9E7682", activeforeground="white",  
            width=5, height=2, padx=5, pady=5, font=("Arial",12)
            )
            
            
        
        row = (i - 1) // 6
        column = (i - 1) % 6
        button.grid(row=row+2, column=column+1, padx=5, pady=5)
        
def validate_entry_ecu(new_value):
    allowed_chars = "0123456789xy√().+-*/^e"
    special_functions = ["sin(", "cos("]

    for func in special_functions:
        while func in new_value:
            new_value = new_value.replace(func, "", 1)

    for char in new_value:
        if char not in allowed_chars:
            return False

    return True


#hace que un campo de texto solo reciba numeros y punto decimal
def validate_entry_decInt(new_value):
        if new_value == "":
            return True
        try:
            float(new_value)
            return True
        except ValueError:
            return False
        
def teclado_euler(root,entry):
    text_var = tk.StringVar()
    button_texts = [
        "7", "8", "9", "/", "x\u207f", "√",
        "4", "5", "6", "=", "x", "e",
        "1", "2", "3", "+", "-", "*",
        "0", ".", "(", ")", "borrar", "clear",
        "sin(", "cos(","y"
    ]
    
    for i, texto in enumerate(button_texts, start=1):
        if texto.isdigit():
            button = tk.Button(
            root, text=texto,
            command=lambda t=texto: button_action_calc(t, text_var, entry),
            bg="#464158", fg="white", 
            activebackground="#9E7682", activeforeground="white",  
            width=5, height=2, padx=5, pady=5,font=("Arial",12)
            )
        else:
            button = tk.Button(
            root, text=texto,
            command=lambda t=texto: button_action_calc(t, text_var, entry),
            bg="#605770", fg="white", 
            activebackground="#9E7682", activeforeground="white",  
            width=5, height=2, padx=5, pady=5, font=("Arial",12)
            )
            
            
        
        row = (i - 1) // 6
        column = (i - 1) % 6
        button.grid(row=row+2, column=column+1, padx=5, pady=5)