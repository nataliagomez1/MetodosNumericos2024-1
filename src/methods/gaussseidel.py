import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-5, max_iter=100):
    n = len(b)
    x = x0 if x0 is not None else np.zeros(n)
    
    for _ in range(max_iter):
        x_new = np.copy(x)
         
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * x_new[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return "La solución del sistema es: " + str(x_new) + "alcanzando la tolerancia "
        
        x = x_new
    
    return "La solución del sistema es: " + str(x)
