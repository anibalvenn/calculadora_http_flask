import os
from typing import Dict


class SegundaCalculadoraViews:
    def segunda_calculadora_view(self, input:dict) -> list:
        self.__clear()
        entrada = input['entrada']

        return entrada

    
    def segunda_calculadora_success(self, lista_float: list, result_final:float) -> None:
        self.__clear()
        calculadora= "Segunda Calculadora"
        status = "sucesso"
        message = '''
            Operaçao realizada com sucesso!
            * Infos:
                Calculadora: {}
                Numeros inseridos: {}
                status: {}
                REsultado final: {}
        '''.format(calculadora, lista_float,status, result_final)
        print(message)

    def segunda_calculadora_fail(self, error: str) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao processar a operacao.
            {}
        '''.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')
