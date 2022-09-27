import unittest
from src.controllers.primeira_calculadora_controller import PrimeiraCalculadoraController

class TestPrimeiraCalculadora(unittest.TestCase):

    def test_primeira_calculadora(self):
        primeira_calculadora = PrimeiraCalculadoraController()
        self.assertEqual(2.541117820166304 , primeira_calculadora.processa_operacao(10)["result"], "deu errado")

if __name__ == "__main__":
        unittest.main()