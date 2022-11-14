from cerberus import Validator


class Validation:

    def __init__(self) -> None:
        self.schema = {
            "numbers": {'type': 'list'}
        }
        self.val = Validator(self.schema)

    def validar(self, document):
        response = self.val.validate(document)
        return response



