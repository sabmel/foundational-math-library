class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0]) if self.rows > 0 else 0

    def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for addition.")
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)])

    def subtract(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)])

    def multiply(self, other):
        if self.columns != other.rows:
            raise ValueError("The number of columns in the first matrix must equal the number of rows in the second matrix.")
        return Matrix([[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns)) for j in range(other.columns)] for i in range(self.rows)])

    def determinant(self):
        if self.rows != self.columns:
            raise ValueError("Determinant can only be calculated for square matrices.")
        # Implement determinant calculation (e.g., using LU decomposition or recursive method)
        pass

    def inverse(self):
        if self.rows != self.columns:
            raise ValueError("Inverse can only be calculated for square matrices.")
        # Implement inverse calculation (e.g., using Gaussian elimination or adjugate method)
        pass

# Utility functions specific to matrices
def print_matrix(matrix):
    for row in matrix.matrix:
        print(' '.join(map(str, row)))

# Example usage
if __name__ == "__main__":
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[5, 6], [7, 8]])

    sum_mat = mat1.add(mat2)
    print("Sum of matrices:")
    print_matrix(sum_mat)

    prod_mat = mat1.multiply(mat2)
    print("\nProduct of matrices:")
    print_matrix(prod_mat)
