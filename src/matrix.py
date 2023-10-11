# matrix.py

def add(m1, m2):
    """Add two matrices."""
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Both matrices must have the same dimensions.")
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

def subtract(m1, m2):
    """Subtract two matrices."""
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Both matrices must have the same dimensions.")
    return [[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

def multiply(m1, m2):
    """Multiply two matrices."""
    if len(m1[0]) != len(m2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    return [[sum(m1[i][k] * m2[k][j] for k in range(len(m1[0]))) for j in range(len(m2[0]))] for i in range(len(m1))]

def transpose(matrix):
    """Return the transpose of a matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def determinant(matrix):
    """Calculate the determinant of a 2x2 or 3x3 matrix."""
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) == 3 and len(matrix[0]) == 3:
        return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
              - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
              + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
    else:
        raise ValueError("Only 2x2 and 3x3 matrices are supported.")

def inverse(matrix):
    """Calculate the inverse of a 2x2 or 3x3 matrix."""
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and has no inverse.")
    
    if len(matrix) == 2:
        adjoint = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]
    else:
        adjoint = [
            [(matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]), -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]), (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])],
            [-(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]), (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]), -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0])],
            [(matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]), -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]), (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])]
        ]
    
    return [[adjoint[i][j] / det for j in range(len(adjoint[0]))] for i in range(len(adjoint))]

