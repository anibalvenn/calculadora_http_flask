

from statistics import variance
from src.drivers.calculation_manager import CalculatorManager
from src.drivers.float_manager import FloatManager


class TerceiraCalculadoraController:

    def __init__(self) -> None:
        self.clc_mng = CalculatorManager()
        self.fl_mng = FloatManager()

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
    
    
        