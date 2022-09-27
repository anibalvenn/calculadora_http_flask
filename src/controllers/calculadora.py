from .interface.calculator import CalculatorInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class Calculator(CalculatorInterface):

    def calculate(self, input: HttpRequest) -> HttpResponse:
        print(input)
        return HttpResponse(status_code=200, body={"ola": "Mundo"})
