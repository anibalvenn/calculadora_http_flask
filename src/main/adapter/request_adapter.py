from typing import Callable, Type

from flask import request as FlaskRequest

from src.main.validate.validation import Validation
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.views_interface import ViewInterface


def request_adapter(request: FlaskRequest, callback: Type[ViewInterface]) -> HttpResponse:
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        query_params=request.args,
        url=request.full_path,
    )

   
    vali = Validation()
     
    valido = vali.validar(http_request.body)
    if valido is True:
        http_response = callback.handle(http_request)
        return http_response
    if valido is False:
        return Exception("xx")
        
        