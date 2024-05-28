"""Implementacion pruebas unitarias"""

import os
import sys

ruta_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(ruta_src)

from methods.puntofijo import fixedpoint
from methods.biseccion import bisection_method
from methods.secante import secante
from methods.newtonraphson import newton_raphson
from methods.gaussseidel import gauss_seidel




import pytest
import math

@pytest.mark.parametrize("function, x0, expected_result", [
    (lambda x: math.sqrt((x + 5)/2), 2, 1.8534870775631227), 
    (lambda x: 0.5 * math.sin(x) + 1, 0.5, 1.4986612937 ),
    (lambda x: (math.cos(x))/3, 0.5, 0.3164984459180211),
    (lambda x: (x**2 - 1)/3, 0.5, -0.3031768798828125),
    (lambda x: math.sqrt(math.sin(x)), 0.5, 0.8725745971801507),
    (lambda x: math.pow(10*x + 5, 1/3), 1.5, 3.3823910122241765),
])
def test_fixedpoint(function, x0, expected_result):
    result = fixedpoint(function, x0)
    assert round(result, 10) == pytest.approx(expected_result, abs=0.000001)

@pytest.mark.parametrize("function, left, right, tol, max_iter, expected_result", [
    (lambda x: x - 2, 0, 4, 1e-6, 100, 2),
    (lambda x: x**2 - 4, 0, 4, 1e-6, 100, 2),
    (lambda x: math.exp(x) - 2, 0, 2, 1e-6, 100, math.log(2)),
    (lambda x: x - 5, 0, 4, 1e-6, 100, None),
    (lambda x: x**3 - 3*x + 1, -1, 1, 1e-4, 100, pytest.approx(0, abs=1e-4)),
    (lambda x: x**3 - 3*x + 1, -1, 1, 1e-10, 5, None)
])
def test_bisection_method(function, left, right, tol, max_iter, expected_result):
    result = bisection_method(function, left, right, tol, max_iter)
    if expected_result is None:
        assert result is None
    else:
        assert abs(result - expected_result) < tol
        



@pytest.mark.parametrize("function, x0, x1, tol, max_iter, expected_result", [
    (lambda x: x - 2, 0, 4, 1e-6, 100, 2),
    (lambda x: x**2 - 4, 1, 3, 1e-6, 100, 2),
    (lambda x: math.exp(x) - 2, 0, 1, 1e-6, 100, math.log(2)),
    (lambda x: x - 5, 0, 4, 1e-6, 5, None),  # Reduciendo el número máximo de iteraciones
    (lambda x: x**3 - 3*x + 1, -1, 1, 1e-6, 100, pytest.approx(0, abs=1e-4)),  # Ajustando la tolerancia
])
def test_secante_method(function, x0, x1, tol, max_iter, expected_result):
    result = secante(function, x0, x1, tol, max_iter)
    if expected_result is None:
        assert result is None
    else:
        assert result == pytest.approx(expected_result, abs=tol)

@pytest.mark.parametrize("function, derivative, x0, expected_result", [
    (lambda x: x**2 - 4, lambda x: 2*x, 2, 2), 
    (lambda x: x**3 - 27, lambda x: 3*x**2, 3, 3),
    (lambda x: math.cos(x), lambda x: -math.sin(x), 0, math.pi/2),
])
def test_newton_raphson(function, derivative, x0, expected_result):
    result = newton_raphson(function, derivative, x0)
    assert result == pytest.approx(expected_result, abs=1e-6)
    
import numpy as np

# Prueba para matriz 4x4 
@pytest.mark.parametrize("A, b, expected_result", [
    (np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]]), 
     np.array([6, 25, -11, 15]), 
     np.array([1.0, 2.0, -1.0, 1.0])),
    (np.array([[4, 1, 2, 0], [3, 5, 1, 1], [1, 1, 3, 1], [0, 2, 1, 4]]), 
     np.array([4, 7, 3, 6]), 
     np.array([0.24, 0.76, 0.41, 1.18])),
    (np.array([[8, 1, 2, 1], [1, 7, 1, 2], [2, 1, 9, 1], [1, 2, 1, 7]]), 
     np.array([8, 7, 9, 7]), 
     np.array([0.5891, 0.5124, 0.7681, 0.4632]))
])
def test_gauss_seidel_4x4(A, b, expected_result):
    result = gauss_seidel(A, b, tol=1e-4, max_iter=1000)
    np.testing.assert_allclose(result, expected_result, rtol=1e-2)

