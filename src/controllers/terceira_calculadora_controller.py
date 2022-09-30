

from statistics import variance
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.drivers.calculation_manager import CalculatorManager
from src.drivers.float_manager import FloatManager
from src.views.terceira_calculadora_view import TerceiraCalculadoraViews


class TerceiraCalculadoraController:

    def __init__(self) -> None:
        self.clc_mng = CalculatorManager()
        self.fl_mng = FloatManager()

    def calculate(self, input: HttpRequest) -> HttpResponse:
        tercCalcView= TerceiraCalculadoraViews()
        entrada = tercCalcView.terceira_calculadora_view(input.body)
        tercCalcControl = TerceiraCalculadoraController()
        saida = tercCalcControl.executa_operacao(entrada)
        if saida['success']:
            return HttpResponse(200, saida)
        else:
            return HttpResponse(500, saida['error'])

    def executa_operacao(self, input):
        input_string = input.split(" ")
        lista_string = []
        for i in input_string:
            lista_string.append(i)
        input_float_list = self.fl_mng.to_float_list(lista_string)
        variancia = self.clc_mng.get_variancia(input_float_list)
        desvio = self.clc_mng.get_desvio_padrao(input_float_list)
        if variancia > desvio:
            return { "success": True, "result": "variancia eh maior", "input": input_float_list }
        else:
            return { "success": False, "result": "desvio padrao eh maior" }
    
    
        