import pytest
import math 

def test_floored_quotient():
    assert 4 // 3 == 1

def test_conversion_of_float_to_int_truncates():
    assert int(4.3) == 4

def test_flooring():
    assert math.floor(4.3) == 4
    assert math.floor(-4.3) == -5

def test_ceil():
    assert math.ceil(4.3) == 5
    assert math.ceil(-4.3) == -4

def test_trunc():
    assert math.trunc(4.3) == 4
    assert math.trunc(4.9) == 4
    assert math.trunc(-4.3) == -4
    assert math.trunc(-4.9) == -4

def test_round():
    assert round(4.5) == 4
    assert round(4.51) == 5
    assert round(4.6) == 5

def test_round_to_places():
    assert round(4.51, 1) == 4.5
    assert round(4.61513, 3) == 4.615