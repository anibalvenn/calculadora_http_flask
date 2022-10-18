from typing import Type
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface
from src.controllers.interface.calculator_interface import CalculatorInterface

class CalculatorView(ViewInterface):
    def __init__(self, controller: Type[CalculatorInterface]) -> None:
        self.__controller = controller

    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        try:
            body = http_request.body
            elements = body["numbers"]

            response = self.__controller.calculate(elements)

            return response
        except Exception as exception:
            return HttpResponse(status_code=500, body={ "error": str(exception) })
