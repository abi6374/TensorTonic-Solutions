import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    a=np.asarray(x,float)
    b=np.asarray(y,float)
    return np.dot(a,b)