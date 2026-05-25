from sympy import sympify


def evaluate_expression(expr):
    try:
        result = sympify(expr).evalf()
        return float(result)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None
