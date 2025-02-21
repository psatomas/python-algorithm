import pytest
from calculator1 import calculator

def test_addition():
    assert calculator(5, 3, '+') == "The addition is 8"

def test_subtraction():
    assert calculator(10, 4, '-') == "The subtraction is 6"

def test_multiplication():
    assert calculator(6, 7, '*') == "The multiplication is 42"

def test_division():
    assert calculator(8, 2, '/') == "The division is 4.0"

def test_division_by_zero():
    assert calculator(5, 0, '/') == "Error: Division by zero"

def test_invalid_operator():
    assert calculator(3, 3, '%') == "Invalid operator"