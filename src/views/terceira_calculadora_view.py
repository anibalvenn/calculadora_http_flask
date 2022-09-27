import os


class TerceiraCalculadoraViews:
    def terceira_calculadora_view(self) -> list:
        self.__clear()

        print('Terceira Calculadora \n\n')
        entrada = input('Digite os numeros com espaço simples entre eles: ')
       
        return entrada
    

    def terceira_calculadora_success(self, lista_float:list, result_final:str) -> None:
        self.__clear()
        calculadora= "Terceira Calculadora"
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

    def terceira_calculadora_fail(self) -> None:
        self.__clear()

        message = '''
            Ocorreu um erro ao executar a operaçao
        '''
        print(message)
    
    def __clear(self):
        os.system('cls||clear')