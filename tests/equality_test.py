import pytest

def test_two_values_point_to_the_same_object_in_memory():
    x = {"a": 1}
    assert x is not {"a": 1}
    assert x is x

def test_value_equality():
    x = {"a": 1}
    assert x == {"a": 1}

def test_equality_overriding():
    class A:
        pass  
    assert A() != A()

    class B:
        def __init__(self, x):
            self.x = x

        def __eq__(self, other):
            if isinstance(other, B):
              return self.x == other.x
            return False
    
    assert B(1) != B(2)
    assert B(1) == B(1)
    assert B(1) != "some other type"
