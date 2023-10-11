# test_matrix.py

from src.matrix import add, subtract, multiply, transpose, determinant, inverse

m2x2_1 = [[1, 2], [3, 4]]
m2x2_2 = [[2, 3], [4, 5]]
        
m3x3_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m3x3_2 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

def test_add():
    assert add(m2x2_1, m2x2_2) == [[3, 5], [7, 9]]
    assert add(m3x3_1, m3x3_2) == [[4, 4, 4], [10, 10, 10], [16, 16, 16]]

def test_subtract():
    assert subtract(m2x2_1, m2x2_2) == [[-1, -1], [-1, -1]]
    assert subtract(m3x3_1, m3x3_2) == [[-2, 0, 2], [-2, 0, 2], [-2, 0, 2]]

def test_multiply():
    assert multiply(m2x2_1, m2x2_2) == [[10, 13], [22, 29]]
    assert multiply(m3x3_1, m3x3_2) == [[30, 26, 22], [84, 71, 58], [138, 116, 94]]

def test_transpose():
    assert transpose(m2x2_1) == [[1, 3], [2, 4]]
    assert transpose(m3x3_1) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

def test_determinant():
    assert determinant(m2x2_1) == -2
    assert determinant(m3x3_1) == 0  # this matrix is singular

def test_inverse():
    assert inverse(m2x2_1) == [[-2, 1], [1.5, -0.5]]
    import pytest
    with pytest.raises(ValueError):
        inverse(m3x3_1)  # this matrix is singular and has no inverse

def test_matrix_dimension_mismatch():
    import pytest
    with pytest.raises(ValueError):
        add(m2x2_1, m3x3_1)
    with pytest.raises(ValueError):
        subtract(m2x2_1, m3x3_1)
    with pytest.raises(ValueError):
        multiply(m2x2_1, m3x3_1)
    with pytest.raises(ValueError):
        determinant([[1, 2, 3], [4, 5, 6]])  # not 2x2 or 3x3

