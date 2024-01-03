from matrix import Matrix
from vector import Vector

def gaussian_elimination(aug_matrix):
    # Implement Gaussian elimination to solve the linear system
    # This is a simplified version and might not cover all edge cases
    n = len(aug_matrix.matrix)

    for i in range(n):
        # Search for maximum in this column
        max_el = abs(aug_matrix.matrix[i][i])
        max_row = i
        for k in range(i+1, n):
            if abs(aug_matrix.matrix[k][i]) > max_el:
                max_el = abs(aug_matrix.matrix[k][i])
                max_row = k

        # Swap maximum row with current row
        aug_matrix.matrix[i], aug_matrix.matrix[max_row] = aug_matrix.matrix[max_row], aug_matrix.matrix[i]

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -aug_matrix.matrix[k][i] / aug_matrix.matrix[i][i]
            for j in range(i, n+1):
                if i == j:
                    aug_matrix.matrix[k][j] = 0
                else:
                    aug_matrix.matrix[k][j] += c * aug_matrix.matrix[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = aug_matrix.matrix[i][n] / aug_matrix.matrix[i][i]
        for k in range(i-1, -1, -1):
            aug_matrix.matrix[k][n] -= aug_matrix.matrix[k][i] * x[i]
    return x

def solve_linear_system(matrix, vector):
    # Create an augmented matrix from A and b
    augmented_matrix = [row + [vector.vector[i]] for i, row in enumerate(matrix.matrix)]
    aug_matrix = Matrix(augmented_matrix)

    # Solve using Gaussian elimination
    return gaussian_elimination(aug_matrix)

# Example usage
if __name__ == "__main__":
    A = Matrix([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
    b = Vector([1, -2, 0])
    solution = solve_linear_system(A, b)
    print("Solution of the system:", solution)

