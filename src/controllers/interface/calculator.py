from abc import ABC, abstractmethod
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class CalculatorInterface(ABC):

    @abstractmethod
    def calculate(self, input: HttpRequest) -> HttpResponse: pass
