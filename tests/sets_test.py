import pytest

def test_superset():
    # returns true if one set is contained within another
    a = {1,2,3,4}
    b = {2,3}

    assert a.issuperset(b)

def test_isdisjoint():
    # returns true if one set is not contained within another
    a = {1,2,3,4}
    b = {2,3}

    assert a.isdisjoint(b) == False
    assert {5,6}.isdisjoint(b)