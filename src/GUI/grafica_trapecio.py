import numpy as np
import matplotlib.pyplot as plt

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

