from src.data import generate_data
from pytest import fixture

@fixture(scope="module")
def data():
    x, y = generate_data(n=100, a=2, b=5) 
    return x, y
