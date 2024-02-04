# test_math_operations.py

from ankurhello.math_operations import add_numbers

def test_add_numbers_positive():
    assert add_numbers(5, 3) == 8

def test_add_numbers_negative():
    assert add_numbers(-5, 3) == -2

def test_add_numbers_floats():
    assert add_numbers(2.5, 3.5) == 6.0

def test_add_numbers_mixed():
    assert add_numbers(2, 3.5) == 5.5
