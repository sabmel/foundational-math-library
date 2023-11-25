# Linear Equations (linear_equations.py)
import numpy as np

def solve_linear_systems(A, b):
    """
    Solves a linear system Ax = b using numpy's linear algebra solver

    Args:
    - A (numpy.ndarray): Coefficient matrix
    - b (numpy.ndarray): Constant terms

    Returns:
    - numpy.ndarray: Solution vector x or error message
    """
    if np.linalg.det(A) == 0:
        return "Cannot solve: Singular matrix"
    
    try:
        return np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return "Linear system cannot be solved due to a singular matrix"

def matrix_inverse(A):
    """
    Computes the inverse of a matrix A using numpy's linear algebra module.

    Args:
    - A (numpy.ndarray): A square matrix

    Returns:
    - numpy.ndarray: Inverse of A or error message
    """
    if np.linalg.det(A) == 0:
        return "Cannot compute inverse: Singular matrix"
    
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return "Cannot compute inverse due to singular matrix"

def matrix_determinant(A):
    """
    Computes the determinant of matrix A.

    Args:
    - A (numpy.ndarray): A square matrix

    Returns:
    - float: Determinant of A
    """
    return np.linalg.det(A)

def matrix_transpose(A):
    """
    Computes the transpose of matrix A.

    Args:
    - A (numpy.ndarray): A matrix

    Returns:
    - numpy.ndarray: Transpose of A
    """
    return np.transpose(A)

# TODO: Add some additional functions: matrix_decomposition, eigenvalues and eigenvectors calculation, etc.

