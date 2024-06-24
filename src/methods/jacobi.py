import numpy as np

def jacobi_method(A, b, x0, tol, max_iterations):
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)

    for k in range(max_iterations):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new*-1

        x = x_new.copy()
    
    print("El método no convergió")
    return x*-1

'''
Toca modificar un poco el metodo para que retorne lo que se necesita para graficar la convergencia del metodo

def jacobi_method(A, b, x0, tol, max_iterations):
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)
    
    # Lista para almacenar las diferencias de norma entre iteraciones sucesivas
    convergence_data = []

    for k in range(max_iterations):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        # Calcular la diferencia de norma entre las iteraciones actuales y anteriores
        norm_diff = np.linalg.norm(x_new - x, ord=np.inf)
        convergence_data.append(norm_diff)

        if norm_diff < tol:
            # Devolver el vector de solución final y los datos de convergencia
            return x_new, convergence_data

        x = x_new.copy()
    
    # Si el método no converge, imprimir un mensaje de advertencia y devolver el último vector de solución y los datos de convergencia
    print("El método no convergió")
    return x, convergence_data

'''