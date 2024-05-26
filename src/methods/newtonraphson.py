import sympy as sp

def newton_raphson(ecuacion, derivada, x0, tolerancia=0.001, max_iter=100):
    
    x = sp.symbols('x')
    
    xi = x0
    
    for cont in range(max_iter):
        ecuacion_evaluada = ecuacion.subs(x, xi).evalf()
        derivada_evaluada = derivada.subs(x, xi).evalf()
        
        if derivada_evaluada == 0:
            print("La derivada en el punto actual es cero, no se puede continuar.")
            return None
        
        xnuevo = xi - ecuacion_evaluada / derivada_evaluada
        error = abs((xnuevo - xi) / xnuevo)
        
        if error < tolerancia:
            return xnuevo
        
        xi = xnuevo
    
    print("Se alcanzó el número máximo de iteraciones sin converger.")
    return None
