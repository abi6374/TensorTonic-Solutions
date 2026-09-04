import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    n=len(v)
    A=np.zeros((n,n))
    for i in range(0,n):
        A[i][i]=v[i]
    return A