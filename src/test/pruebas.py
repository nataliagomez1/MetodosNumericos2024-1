"""Implementacion pruebas unitarias"""

import pytest
import math
from methods.puntofijo import fixedpoint 

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