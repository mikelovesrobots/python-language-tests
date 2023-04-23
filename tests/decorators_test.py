import pytest

def test_decorator():
    def plusone(func):
        def inner(*args, **kwargs):
            return 1 + func(*args, **kwargs)
        return inner
    
    @plusone
    def x(y):
        return y
    
    assert x(1) == 2
         