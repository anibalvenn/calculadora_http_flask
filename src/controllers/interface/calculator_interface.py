from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from typing import List


class CalculatorInterface(ABC):

    @abstractmethod
    def calculate(self, elements: List[float]) -> float:
        pass