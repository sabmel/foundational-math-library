# vector.py

def validate_vector(vector):
    """
    Validate that the input is a vector (a list of numbers).

    Parameters:
    vector: list of numbers
    """
    if not isinstance(vector, list) or not all(isinstance(x, (int, float)) for x in vector):
        raise TypeError("Input must be a list of numbers.")

def add(v1, v2):
    """
    Add two vectors.
    
    Parameters:
    v1, v2: list of numbers
    
    Returns:
    List of numbers representing the vector sum.
    """
    validate_vector(v1)
    validate_vector(v2)
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
    validate_vector(v1)
    validate_vector(v2)
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
    validate_vector(v1)
    validate_vector(v2)
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
    Float representing the magnitude of the vector.
    """
    validate_vector(vector)
    return sum(x**2 for x in vector)**0.5

def normalize(vector):
    """
    Normalize a vector to unit length.

    Parameters:
    vector: list of numbers

    Returns:
    List of numbers representing the normalized vector.
    """
    validate_vector(vector)
    mag = magnitude(vector)
    if mag == 0:
        raise ValueError("Cannot normalize a zero vector.")
    return [x / mag for x in vector]

def angle_between(v1, v2):
    """
    Calculate the angle (in degrees) between two vectors.

    Parameters:
    v1, v2: list of numbers

    Returns:
    Float representing the angle in degrees between the two vectors/
    """
    validate_vector(v1)
    validate_vector(v2)
    if len(v1) != len(v2):
        raise ValueError("Both vectors must have the same length.")
    
    dot_prod = dot_product(v1, v2)
    mag_v1 = magnitude(v1)
    mag_v2 = magnitude(v2)

    if mag_v1 * mag_v2 == 0:
        raise ValueError("Cannot calculate angle with a zero vector.")
    
    # Calculate the cosine of the angle
    cos_angle = dot_prod / (mag_v1 * mag_v2)

    # Ensure the cosine value is within valid range to handle floating point errors
    cos_angle = max(min(cos_angle, 1.0), -1.0)

    # convert to degrees
    angle_in_radians = math.acos(cos_angle)
    angle_in_degrees = math.degrees(angle_in_radians)

    return angle_in_degrees
