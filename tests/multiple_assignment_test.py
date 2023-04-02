import pytest

def test_multiple_assignment():
    a, b = 1, 2
    a, b = b, a + b
    assert a == 2
    assert b == 3
    