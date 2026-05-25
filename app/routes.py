from flask import Blueprint, request, jsonify, render_template
from .nlp_parser import parse_math_query
from .calculator import evaluate_expression

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("chat.html")


@main_bp.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(force=True)
    user_query = data.get("message", "")
    expression = parse_math_query(user_query)
    if expression is None:
        response = {"error": "Maaf, saya tidak mengerti pertanyaan Anda."}
    else:
        result = evaluate_expression(expression)
        if result is None:
            response = {"error": "Terjadi kesalahan perhitungan."}
        else:
            response = {"result": result}
    return jsonify(response)
