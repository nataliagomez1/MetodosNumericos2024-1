def secante(f, x0, x1, tol=1e-5, max_iter=100, return_points=False):
    x_vals = [x0, x1]
    y_vals = [f(x0), f(x1)]
    
    for _ in range(max_iter):
        if f(x1) == f(x0):
            raise ValueError("La función no puede ser evaluada en los puntos proporcionados.")
        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        y2 = f(x2)
        
        x_vals.append(x2)
        y_vals.append(y2)
        
        if abs(x2 - x1) < tol:
            break
        
        x0, x1 = x1, x2
    
    if return_points:
        return x_vals, y_vals
    else:
        return x2
