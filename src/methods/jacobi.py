import numpy as np

def jacobi_method(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    x_new = np.zeros_like(x)
    for _ in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new.copy()
    raise Exception(f"No se alcanzó la convergencia después de {max_iter} iteraciones")