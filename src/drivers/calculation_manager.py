from unittest import result
import numpy as np

class CalculatorManager:
    def __init__(self)->None:
        self.__np = np

    def raiz_quadrada_positiva(self, input)->float:
        root = self.__np.sqrt(input)
        return root
     

    def potenciar(self, base, expoente)->float:
        potencia = self.__np.power(base, expoente)
        return potencia

    def media_de_tres(self, t1:float, t2:float, t3:float)->float:
        media = self.__np.average([t1, t2, t3])
        return media

    def get_desvio_padrao(self, input:list)->float:
        std = self.__np.std(input)
        return std

    def get_variancia(self, input:list)->float:
        variancia = self.__np.var(input)
        return variancia