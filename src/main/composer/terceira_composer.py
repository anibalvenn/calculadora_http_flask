from src.views.calculator_view import CalculatorView
from src.controllers.terceira_calculadora_controller import TerceiraCalculadoraController

def calculator_composer_terceira():
    calculator_controller = TerceiraCalculadoraController()
    calculator_view = CalculatorView(calculator_controller)
    return calculator_view
