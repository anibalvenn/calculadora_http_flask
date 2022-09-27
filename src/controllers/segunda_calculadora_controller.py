from queue import Empty
from typing import Dict, List
from unittest import result

from src.drivers.calculation_manager import CalculatorManager
from src.drivers.float_manager import FloatManager

class SegundaCalculadoraController:

    def __init__(self) -> None:
        self.clc_mng = CalculatorManager()
        self.fl_mng = FloatManager()

    def executa_operacao(self, input: list):
        try:
            passo1 = self.__multiplica11(input)
            result = self.__get_std_inverter(passo1)     
            
            return { "success": True, "result": result, "input": input }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __multiplica11(self, input: list) -> list:
        output2 = []
        if input is Empty: raise Exception('Lista vazia!')
        input_float = self.fl_mng.to_float_list(input)
        
        if input_float is Empty: raise Exception('Lista vazia!')
        for a in input_float:
            b = a*11
            c = self.clc_mng.potenciar(b, 0.95)
            output2.append(c)
        
        return output2        

    def __get_std_inverter(self, input) -> float:
        desvio = self.clc_mng.get_desvio_padrao(input)
        result = 1/desvio
        return result
