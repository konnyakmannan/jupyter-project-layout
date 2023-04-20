import numpy as np

def zero_padding(x: int, width: int) -> str:
    result = str(x).zfill(width)
    return result
