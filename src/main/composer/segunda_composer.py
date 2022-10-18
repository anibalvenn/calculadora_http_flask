from src.views.calculator_view import CalculatorView
from src.controllers.segunda_calculadora_controller import SegundaCalculadoraController

def calculator_composer_segunda():
    calculator_controller = SegundaCalculadoraController()
    calculator_view = CalculatorView(calculator_controller)
    return calculator_view
