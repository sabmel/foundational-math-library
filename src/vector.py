# vector.py

def add(v1, v2):
    """
    Add two vectors.
    
    Parameters:
    v1: list of numbers
    v2: list of numbers
    
    Returns:
    result: list of numbers
    """
    if len(v1) != len(v2):
        raise ValueError("Both vectors must have the same length.")
    return [v1[i] + v2[i] for i in range(len(v1))]

def subtract(v1, v2):
    """
    Subtract two vectors.
    
    Parameters:
    v1: list of numbers
    v2: list of numbers
    
    Returns:
    result: list of numbers
    """
    if len(v1) != len(v2):
        raise ValueError("Both vectors must have the same length.")
    return [v1[i] - v2[i] for i in range(len(v1))]

def dot_product(v1, v2):
    """
    Calculate the dot product of two vectors.
    
    Parameters:
    v1: list of numbers
    v2: list of numbers
    
    Returns:
    result: float or int
    """
    if len(v1) != len(v2):
        raise ValueError("Both vectors must have the same length.")
    return sum([v1[i] * v2[i] for i in range(len(v1))])

def scalar_multiply(scalar, vector):
    """
    Multiply a vector by a scalar.
    
    Parameters:
    scalar: float or int
    vector: list of numbers
    
    Returns:
    result: list of numbers
    """
    return [scalar * i for i in vector]

def magnitude(vector):
    """
    Calculate the magnitude (norm) of a vector.
    
    Parameters:
    vector: list of numbers
    
    Returns:
    result: float
    """
    return (sum([i**2 for i in vector]))**0.5
