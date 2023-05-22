import numpy as np

def generate_data(n, a, b):
    x= np.random.uniform(size=n)
    noise = np.random.normal(scale=0.1, size=n)
    y = a*x  +b + noise
    return x, y
