# tests/test_calculator.py

from app.calculator import evaluate_expression


def test_addition():
    assert evaluate_expression("5+2") == 7.0


def test_multiplication():
    assert evaluate_expression("7*8") == 56.0


def test_division():
    assert evaluate_expression("100/4") == 25.0


def test_power():
    assert evaluate_expression("5**2") == 25.0


def test_invalid_expression():
    assert evaluate_expression("5***") is None
