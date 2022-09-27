from flask import request, jsonify
from src.main.adapter.request_adapter import request_adapter
from src.controllers.calculadora import Calculator
from .server import app


@app.route("/", methods=["POST"])
def calculator_function():
    http_response = request_adapter(request, Calculator())
    return jsonify(http_response.body), http_response.status_code 
