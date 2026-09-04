import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    a=0
    for i in range(0,len(A)):
        a+=A[i][i]
    return float(a)