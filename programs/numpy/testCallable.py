import numpy as np
from typing import Callable

def deriv(func: Callable[[ndarray], ndarray], 
          input_: ndarray,
          delta: float = 0.001) -> ndarray:
    return (func(input_ + delta) - func(input_ - delta))/ (2*delta)


