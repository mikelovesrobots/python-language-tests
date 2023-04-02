import pytest

def test_printf_style_formatting():
    assert "This is my number %.2f" % 1 == "This is my number 1.00"

def test_mapping_style_keys():
    assert "this is my number %(number).2f" % {"number": 1} == "this is my number 1.00"