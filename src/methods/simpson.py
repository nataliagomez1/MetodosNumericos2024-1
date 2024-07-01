def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser par")
    
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)
    
    for i in range(2, n, 2):
        suma += 2 * f(a + i * h)
    
    return (h / 3) * suma
