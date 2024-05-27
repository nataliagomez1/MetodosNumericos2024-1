def secante(f, x0, x1, tol=1e-5, max_iter=100):
    """
    Implementación del método de la secante para encontrar una raíz de la función f.

    Parámetros:
    f : función
        La función para la cual estamos buscando una raíz.
    x0, x1 : float
        Las dos aproximaciones iniciales para la raíz.
    tol : float, opcional
        La tolerancia para la convergencia. La iteración se detiene si el valor absoluto de f(x) es menor que tol.
    max_iter : int, opcional
        El número máximo de iteraciones permitidas.

    Retorna:
    float
        Una aproximación a la raíz de la función, o None si no se encuentra la raíz dentro del número máximo de iteraciones.

    Lanza:
    ValueError
        Si hay una división por cero en la iteración.
    """
    
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 == f_x0:
            raise ValueError("Error: División por cero en la iteración número {}.".format(i))

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(f(x2)) < tol:
            return x2

        if abs(x2 - x1) < tol:
            return x2

        x0, x1 = x1, x2

    return None

