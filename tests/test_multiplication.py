
from example_python_package import multiply_two_numbers

def test_multiplication_small_numbers():
    result = multiply_two_numbers(5, 6)
    assert result == 30

def test_multiplication_large_numbers():
    result = multiply_two_numbers(100, 300)
    assert result == 30000