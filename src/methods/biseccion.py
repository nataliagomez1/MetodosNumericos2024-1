def bisection_method(function, left, right, tol, max_iter):
    """
    Encuentra la raíz de la función f en el intervalo [a, b] usando el método de bisección.
    
    Args:
        function (function): La función de la cual encontrar la raíz.
        left (float): Extremo izquierdo del intervalo.
        right (float): Extremo derecho del intervalo.
        tol (float): Tolerancia: criterio de convergencia (precisión deseada).
        max_iter (int): Número máximo de iteraciones permitidas.
        
    Returns:
        float: La aproximación de la raíz de f.
    """
    if function(left) * function(right) >= 0:
        return None
    
    iter_count = 0
    while (right - left) / 2 > tol:
        medium = (left + right) / 2
        
        if function(medium) == 0:
            return medium
        
        if function(medium) * function(left) < 0:
            right = medium  
        else:
            left = medium  
        
        iter_count += 1
        
        if iter_count > max_iter:
            return None
    
    return (left + right) / 2