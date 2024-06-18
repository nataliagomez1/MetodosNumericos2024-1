import matplotlib.pyplot as plt

def graf_convergencia_jacobi(norm_diff_list, tol):
    plt.plot(range(1, len(norm_diff_list) + 1), norm_diff_list, marker='o', linestyle='-')
    plt.xlabel('Número de Iteraciones')
    plt.ylabel('Norma del Cambio')
    plt.title('Convergencia del Método')
    plt.axhline(y=tol, color='r', linestyle='--', label='Tolerancia')
    plt.legend()
    plt.grid(True)
    plt.show()
