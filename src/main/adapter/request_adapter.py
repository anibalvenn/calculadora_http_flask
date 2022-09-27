from flask import request as FlaskRequest
from src.controllers.primeira_calculadora_controller import PrimeiraCalculadoraController
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.controllers.interface.calculator import CalculatorInterface
from src.views.primeira_calculadora_view import PrimeiraCalculadoraViews
from src.views.segunda_calculadora_view import SegundaCalculadoraViews
from src.views.terceira_calculadora_view import TerceiraCalculadoraViews

def request_adapter(request: FlaskRequest, calculator: CalculatorInterface) -> HttpResponse:
    
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        query_params=dict(request.args),
        path_params=request.view_args,
        url=request.full_path,
        ipv4=request.remote_addr,
    )

    if http_request.body["calculadora"] == '1':
        primCalcControl = PrimeiraCalculadoraController()
        return primCalcControl.calculate()

    elif http_request.body["calculadora"] == '2':
        segCalcView= SegundaCalculadoraViews()
        entrada = segCalcView.segunda_calculadora_view(http_request.body)
    elif http_request.body["calculadora"] == '3':
       tercCalcView=TerceiraCalculadoraViews()
       entrada = tercCalcView.terceira_calculadora_view(http_request.body)
    

    http_response = calculator.calculate(http_request)
    return http_response
