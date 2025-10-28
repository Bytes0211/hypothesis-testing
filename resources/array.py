
import numpy as np
import sympy as sp
import array


class Array:
    
    def __init__(self, label: str = "new_array"):
        self.name = label
    
    def get_array(self, low: int, high: int, size: tuple) -> tuple:
        arr = np.random.randint(low = low, high = high, size = size)
        matrix = sp.Matrix(arr)
        return arr, matrix
    
    