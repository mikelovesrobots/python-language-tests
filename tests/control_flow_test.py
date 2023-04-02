import pytest

def test_if_statements():
    a = 1
    if a == 1:
        assert 1 == 1
    elif a == 2:
        assert 2 == 2
    else:
        assert 3 == 3

def test_iterating_over_a_list():
    x = [1,2,3]
    y = []
    for number in x:
        y.append(number)
    assert y == [1,2,3]

def test_iterating_over_a_dict():
    a = {"a": 1}
    b = {}
    for k, v in a.items():
        b[k] = v
    assert b == a

def test_iterating_n_times():
    a = 0
    for x in range(5):
        a += 1
    assert a == 5

def test_iterating_over_indices():
    a = [1,2,3]
    b = 0
    for i in range(len(a)):
        b += a[i]
    assert b == 6


    