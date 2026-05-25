# tests/test_parser.py

from app.nlp_parser import parse_math_query


def test_addition():
    assert parse_math_query("5+2") == "5+2"


def test_multiplication():
    assert parse_math_query("7*8") == "7*8"


def test_division():
    assert parse_math_query("100 dibagi 4") == "100/4"


def test_invalid_input():
    assert parse_math_query("halo apa kabar") is None
