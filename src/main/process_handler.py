from .constructor.introduction_page_process import introduction_process
from .constructor.primeira_calculadora_process import primeira_calculadora_process
from .constructor.segunda_calculadora_process  import segunda_calculadora_process
from .constructor.terceira_calculadora_process import terceira_calculadora_process


def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': primeira_calculadora_process()
        elif command == '2': segunda_calculadora_process()
        elif command == '3': terceira_calculadora_process()
        elif command == '4': exit()
        else: print('\nComando nao encontrado, tente novamente!\n\n')
