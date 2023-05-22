from src.lr import estimate_coef

def test_estimate_coef(data):
    x, y = data
    b0, b1 = estimate_coef(x, y)
    assert b0 is float
    assert b1 is float
