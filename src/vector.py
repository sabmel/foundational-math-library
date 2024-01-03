import math

class Vector:
    def __init__(self, vector):
        self.vector = vector

    def dot_product(self, other):
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must be of the same length for dot product.")
        return sum(a * b for a, b in zip(self.vector, other.vector))

    def cross_product(self, other):
        if len(self.vector) != 3 or len(other.vector) != 3:
            raise ValueError("Cross product is defined only for 3D vectors.")
        a1, a2, a3 = self.vector
        b1, b2, b3 = other.vector
        return Vector([a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1])

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.vector))

# Utility functions specific to vectors
def print_vector(vector):
    formatted_vector = ', '.join(map(str, vector.vector))
    print(f"<{formatted_vector}>")

# Example usage
if __name__ == "__main__":
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([4, 5, 6])

    dot_prod = vec1.dot_product(vec2)
    print("Dot product of vec1 and vec2:", dot_prod)

    cross_prod = vec1.cross_product(vec2)
    print("Cross product of vec1 and vec2:")
    print_vector(cross_prod)

