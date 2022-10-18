from src.views.calculator_view import CalculatorView
from src.controllers.primeira_calculadora_controller import PrimeiraCalculadoraController


def calculator_composer_primeira():
    calculator_controller = PrimeiraCalculadoraController()
    calculator_view = CalculatorView(calculator_controller)
    return calculator_view
