from urllib import response
from src.views.terceira_calculadora_view import TerceiraCalculadoraViews
from src.controllers.terceira_calculadora_controller import TerceiraCalculadoraController

def terceira_calculadora_process() -> None:
    terceira_calculadora_view = TerceiraCalculadoraViews()
    terceira_calculadora_controller = TerceiraCalculadoraController()

    entrada = terceira_calculadora_view.terceira_calculadora_view()
    saida = terceira_calculadora_controller.executa_operacao(entrada)

    if saida["success"]: terceira_calculadora_view.terceira_calculadora_success(saida["input"], saida["result"])
    else: terceira_calculadora_view.terceira_calculadora_fail()

