import pytest

def test_simple_formatted_string_literals():
    x = 'abc'
    assert f"x is {x}" == "x is abc"

def test_representation_flag():
    x = "abc"
    assert f"x is {x!r}" == "x is 'abc'"
    y = {"a": 1}
    assert f"y is {y!r}" == "y is {'a': 1}"
    assert f"y is {repr(y)}" == "y is {'a': 1}"

def test_debugging():
    x = "abc"
    assert f"{x=}" == "x='abc'"

def test_whitespace():
    x = "abc"
    assert f"x is { x }" == "x is abc"

