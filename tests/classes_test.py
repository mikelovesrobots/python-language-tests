import pytest

def test_minimalistic_class():
    class A:
        pass
    assert isinstance(A(), A)
    assert isinstance(A(), object)

def test_subclass():
    class A:
        pass
    class B(A):
        pass
    assert issubclass(B, A)
        
def test_properties():
    class A:
        x = 1

        def __init__(self):
            self.y = 1

    a = A()
    assert a.x == 1

    a.x = 2
    assert a.x == 2

    assert a.y == 1

def test_deleting_properties():
    class A:
        x = 1

        def __init__(self):
            self.y = 1

    a = A()
    with pytest.raises(AttributeError):
      # note, you can't delete a class attribute
      del a.x

    # but you can delete instance attributes
    del a.y
    with pytest.raises(AttributeError): 
        a.y

def test_initializers():
    class A:
        def __init__(self):
            self.x = 1
    assert A().x == 1

def test_initializers_with_arguments():
    class A:
        def __init__(self, x):
            self.x = x
    assert A(1).x == 1

def test_str():
    class A:
        def __str__(self):
            return "this is my string conversion"    
    assert str(A()) == "this is my string conversion"

def test_methods():
    class A:
        x = 1
        def y(self):
            return self.x

    assert A().y() == 1

def test_private_methods():
    # Python "mangles" private method names
    class A:
        def __x(self):
            return 1
    
    assert A()._A__x() == 1

    with pytest.raises(AttributeError):
      # Note this doesn't work
      A().__x()

def test_deleting_objects():
    class A:
        pass
    a = A()
    del a
    with pytest.raises(UnboundLocalError):
        a

def test_property_getters_and_setters():
    class A:
        def __init__(self):
            self.y = 1

        @property
        def x(self):
            return self.y
        
        @x.setter
        def x(self, value):
            self.y = value
            return self.y
        
    a = A()
    assert a.x == 1

    a.x = 2
    assert a.x == 2
  

        