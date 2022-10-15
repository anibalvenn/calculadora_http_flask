from flask import request, jsonify
from src.controllers.terceira_calculadora_controller import TerceiraCalculadoraController
from src.controllers.segunda_calculadora_controller import SegundaCalculadoraController
from src.main.adapter.request_adapter import request_adapter
from .server import app
from src.controllers.primeira_calculadora_controller import PrimeiraCalculadoraController


@app.route("/1", methods=["POST"])
def calculator_function():
    primCalcControl = PrimeiraCalculadoraController()        
    http_response = request_adapter(request, primCalcControl)
    return jsonify(http_response.body), http_response.status_code 

@app.route("/2", methods=["POST"])
def calculator_function_2():
    segCalcControl = SegundaCalculadoraController()        
    http_response = request_adapter(request, segCalcControl)
    return jsonify(http_response.body), http_response.status_code 

@app.route("/3", methods=["POST"])
def calculator_function_3():
    tercCalcControl = TerceiraCalculadoraController()        
    http_response = request_adapter(request, tercCalcControl)
    return jsonify(http_response.body), http_response.status_code 
