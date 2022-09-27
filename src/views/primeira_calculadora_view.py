import os

class PrimeiraCalculadoraViews:
    def primeira_calculadora_view(self) -> str:
        self.__clear()

        print('Primeira Calculadora \n\n')
        entrada = input('Digite o numero: ')

        return entrada
    
    def primeira_calculadora_success(self, entrada: float, result_final:float) -> None:
        self.__clear()
        calculadora= "Primeira Calculadora"
        status = "sucesso"
        message = '''
            Operaçao realizada com sucesso!
            * Infos:
                Calculadora: {}
                Numero inserido: {}
                status: {}
                REsultado final: {}
        '''.format(calculadora, entrada,status, result_final)
        print(message)
    
    def primeira_calculadora_fail(self, error: str) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao executar a operação.
            {}
        '''.format(error)
        print(message)

    def __clear(self):
        os.system('cls||clear')
