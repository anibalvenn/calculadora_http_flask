import os
from typing import Dict


class SegundaCalculadoraViews:
    def segunda_calculadora_view(self) -> list:
        self.__clear()

        print('Segunda Calculadora \n\n')
        entrada = input('Digite os numeros com espaço simples entre eles: ')
        entrada_split = entrada.split(" ")
        lista_float = []
        for i in entrada_split:
            item_float = float(i)
            lista_float.append(item_float)


        return lista_float
    
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
