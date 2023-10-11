# test_vector.py
print("Test file is being executed!")

from src.vector import add, subtract, dot_product, scalar_multiply, magnitude

v1 = [1, 2, 3]
v2 = [4, 5, 6]
scalar = 3

def test_add():
    assert add(v1, v2) == [5, 7, 9]

def test_subtract():
    assert subtract(v1, v2) == [-3, -3, -3]

def test_dot_product():
    assert dot_product(v1, v2) == 32

def test_scalar_multiply():
    assert scalar_multiply(scalar, v1) == [3, 6, 9]

def test_magnitude():
    assert magnitude(v1) == 3.7416573867739413

def test_vector_length_mismatch():
    import pytest
    with pytest.raises(ValueError):
        add([1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        subtract([1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        dot_product([1, 2], [1, 2, 3])
