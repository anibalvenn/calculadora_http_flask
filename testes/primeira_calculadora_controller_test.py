from src.controllers.primeira_calculadora_controller import PrimeiraCalculadoraController
from faker import Faker

fake = Faker()

def test_prim_calc():
    calc = PrimeiraCalculadoraController()
    ran = fake.random_number()
    expect = ran/3
    
    result = calc.divide_por_tres(ran)

    assert result == expect

test_prim_calc()
