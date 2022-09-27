class FloatManager:

    def __init__(self) -> None:
        pass

    def to_float_list(self, input:list)->list:
        output1 = []
        for i in input:
            try:
                a = float(i)
                output1.append(a)
            except Exception as exception:
                return {"success": False, "error":"nao eh uma lista float"}
        return output1

    def to_float(self, input:str)->float:
            try:
                a = float(input)
            except Exception as exception:
                return {"success": False, "error":"nao eh um float"}
            return a