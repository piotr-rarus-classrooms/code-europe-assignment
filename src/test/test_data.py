from src.data import generate_data


def test_generate_data() -> None:
    x, y = generate_data(n=100, a=2, b=5) 
    assert x.shape == (100,)
    assert y.shape == (100,)
    assert x.max() <= 1
    assert y.max() <= 10
