from src.controllers.interface.calculator_interface import CalculatorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from typing import List


class Calculator(CalculatorInterface):

    def calculate(self, elements: List[float]) -> float:
        self.__validate(elements)

        elem1 = elements[0]
        elem2 = elements[1]

        return elem1 + elem2


    def __validate(self, elements) -> None:
        if (
            not isinstance(elements[0], float)
            or not isinstance(elements[1], float)
        ): raise Exception('Value Errors')
