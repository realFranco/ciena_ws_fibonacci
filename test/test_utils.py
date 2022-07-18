"""
Testing the utils package.

Examples of execution

pytest test -s -v  # General testing

pytest test/test_utils.py -s -v  # Specific testing
"""
from core.utils import Computation, DataManagement


def test_fibonacci():
    out = Computation.fibonacci_in_range(1, 9)
    assert out == [1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_sanitize_ok():
    data = {'l': 1, 'r': 9}
    left, right = DataManagement.sanitize_data(data)
    assert left == data['l'] and right == data['r']

def test_sanitize_empty_data():
    data = {}
    left, right = DataManagement.sanitize_data(data)
    assert left == 0 and right == 0

def test_sanitize_signed_integers():
    data = {'l': -1, 'r': -9}
    left, right = DataManagement.sanitize_data(data)
    assert left == 0 and right == 0