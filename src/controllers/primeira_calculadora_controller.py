from numpy import float
from msilib import CAB
from typing import Dict
from unittest import result
from src.drivers.calculation_manager import CalculatorManager
from src.drivers.float_manager import FloatManager

class PrimeiraCalculadoraController:

    def __init__(self) -> None:
        self.clc_mng = CalculatorManager()

    def processa_operacao(self, input: str):
        try:
            fl_mng = FloatManager()
            input_float= fl_mng.to_float(input)
            divide_por_tres= self.__divide_por_tres(input_float)
            primeiro_algarismo = self.__primeira_operacao(divide_por_tres)
            segundo_algarismo = self.__segunda_operacao(divide_por_tres)
            terceiro_algarismo = divide_por_tres

            media = self.clc_mng.media_de_tres(primeiro_algarismo, segundo_algarismo, terceiro_algarismo)
            return { "success": True, "result": media, "input": input_float}


        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __divide_por_tres(self, input: str) -> float:

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