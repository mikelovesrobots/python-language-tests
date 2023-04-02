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


def test_early_break():
    for i in range(10):
        if i == 5:
            break
    assert i == 5

def test_else():
    for i in range(10):
        pass
    else:
        # Only runs on normal completion
        i = 0
    assert i == 0

def test_early_break_else():
    for i in range(10):
        if i == 5:
            break
    else:
        # Only runs on normal completion
        i = 0
    assert i == 5


def test_while_loop():
    a = 10
    while a > 0:
        a -= 1
    assert a == 0
    
def test_match_switch_statements():
    x = 1
    match 1:
        case 1:
            x = 2
        case _:
            x = 3
    assert x == 2

    match 2:
        case 1:
            x = 2
        case _:
            x = 3
    assert x == 3
