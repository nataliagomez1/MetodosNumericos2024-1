import numpy as np

def gauss_seidel(A, b, x0, tol=1e-5, max_iter=100):
    n = len(A)
    x = x0.copy()
    
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1
        
        x = x_new
    
    raise Exception("El método no converge después de las iteraciones máximas")