

from statistics import variance
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.drivers.calculation_manager import CalculatorManager
from src.drivers.float_manager import FloatManager


class TerceiraCalculadoraController:

    def __init__(self) -> None:
        self.clc_mng = CalculatorManager()
        self.fl_mng = FloatManager()

    def calculate(self, input: list) -> HttpResponse:

        tercCalcControl = TerceiraCalculadoraController()
        saida = tercCalcControl.executa_operacao(input)
        if saida['success']:
            return HttpResponse(200, saida)
        else:
            return HttpResponse(500, saida['error'])

    def executa_operacao(self, input_float_list):
        if len(input_float_list)<=1: raise Exception('Input com pelo menos dois numeros')

 
        variancia = self.clc_mng.get_variancia(input_float_list)
        desvio = self.clc_mng.get_desvio_padrao(input_float_list)
        if variancia > desvio:
            return { "success": True, "result": "variancia eh maior", "input": input_float_list }
        else:
            return { "success": False, "result": "desvio padrao eh maior" }
    
    
        