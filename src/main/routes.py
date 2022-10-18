from flask import Blueprint, request, jsonify
calculator_routes_bp = Blueprint("api_routes", __name__)

from src.main.adapter.request_adapter import request_adapter

from src.main.composer.primeira_composer import calculator_composer_primeira
from src.main.composer.segunda_composer import calculator_composer_segunda
from src.main.composer.terceira_composer import calculator_composer_terceira


@calculator_routes_bp.route("/1", methods=["POST"])
def calculate():
    http_response = request_adapter(request, calculator_composer_primeira())
    return jsonify(http_response.body), http_response.status_code

@calculator_routes_bp.route("/2", methods=["POST"])
def calculate2():
    http_response = request_adapter(request, calculator_composer_segunda())
    return jsonify(http_response.body), http_response.status_code

@calculator_routes_bp.route("/3", methods=["POST"])
def calculate3():
    http_response = request_adapter(request, calculator_composer_terceira())
    return jsonify(http_response.body), http_response.status_code
