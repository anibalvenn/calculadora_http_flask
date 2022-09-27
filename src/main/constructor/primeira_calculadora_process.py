from src.views.primeira_calculadora_view import PrimeiraCalculadoraViews
from src.controllers.primeira_calculadora_controller import PrimeiraCalculadoraController

def primeira_calculadora_process() -> None:
    primeira_calculadora_views = PrimeiraCalculadoraViews()
    primeira_calculadora_controller = PrimeiraCalculadoraController()

    entrada = primeira_calculadora_views.primeira_calculadora_view()
    response = primeira_calculadora_controller.processa_operacao(entrada)

    if response["success"]: primeira_calculadora_views.primeira_calculadora_success(response["input"],response["result"],)
    else: primeira_calculadora_views.primeira_calculadora_fail(response["error"])

