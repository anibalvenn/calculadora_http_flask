from src.views.segunda_calculadora_view import SegundaCalculadoraViews
from src.controllers.segunda_calculadora_controller import SegundaCalculadoraController

def segunda_calculadora_process() -> None:
    segunda_calculadora_views = SegundaCalculadoraViews()
    segunda_calculadora_controller = SegundaCalculadoraController()

    entrada = segunda_calculadora_views.segunda_calculadora_view()
    response = segunda_calculadora_controller.executa_operacao(entrada)

    if response["success"]: segunda_calculadora_views.segunda_calculadora_success(response["input"], response["result"])
    else: segunda_calculadora_views.segunda_calculadora_fail(response["error"])

