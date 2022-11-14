from urllib import response
from src.controllers.calculadora import Calculator
from numpy import float
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.drivers.calculation_manager import CalculatorManager
from src.drivers.float_manager import FloatManager

class PrimeiraCalculadoraController(Calculator):

    def __init__(self) -> None:
        self.clc_mng = CalculatorManager()

    
    def calculate(self, input: list) -> HttpResponse:
 
        if len(input)==1:
            primCalcControl = PrimeiraCalculadoraController()
            saida = primCalcControl.processa_operacao(input[0])
            if saida['success']:
                return HttpResponse(200, saida)
            else:
                return HttpResponse(500, saida['error'])
        else:
            raise Exception("O input deve conter apenas um numero") 



    def processa_operacao(self, input_float: float):
        try:
           
            divide_por_tres= self.divide_por_tres(input_float)
            primeiro_algarismo = self.__primeira_operacao(divide_por_tres)
            segundo_algarismo = self.__segunda_operacao(divide_por_tres)
            terceiro_algarismo = divide_por_tres

            media = self.clc_mng.media_de_tres(primeiro_algarismo, segundo_algarismo, terceiro_algarismo)
            return { "success": True, "result": media, "input": input_float}


        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def divide_por_tres(self, input: str) -> float:

        result = input/3

        return result

    def __primeira_operacao(self, input: float)-> float:
        
        divide4soma7 = self.__divide4soma7(input)
        result = self.__raiz_quadrada_multiplica_constante(divide4soma7)
        return result
      
    def __divide4soma7(self, input: float) -> float:

        result = input/4 +7

        return result

    def __raiz_quadrada_multiplica_constante(self, input: float) -> float:

        result = self.clc_mng.raiz_quadrada_positiva(input)*.257

        return result
    
    def __segunda_operacao(self, input)->float:
        result = self.clc_mng.potenciar(input, 2.121)/5 +1
        return result