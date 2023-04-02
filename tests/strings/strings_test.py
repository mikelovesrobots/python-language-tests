import pytest

def test_raw_strings():
    assert r'\n'[0] == "\\"

def test_multiline_strings():
    x = """\
Here is some text\
and more text\
"""
    assert x == "Here is some textand more text"
    y = """
Here is some text
and more text
"""
    assert y == "\nHere is some text\nand more text\n"

def test_concatenation():
    assert 'a' + 'b' == 'ab'
    assert 'a' 'b' == 'ab' 
    assert ('a long string'
    'another long string') == 'a long stringanother long string'


def test_indexing():
    assert 'ab'[0] == 'a'
    assert 'ab'[-1] == 'b'
    assert 'ab'[-2] == 'a' 
    with pytest.raises(IndexError):
        assert 'ab'[-3] == 'b'

def test_slicing():
    assert 'abc'[0:1] == 'a' # characters from position 0 through and excluding position 1
    assert 'abc'[0:] == 'abc' # characters from position 0 to the end
    assert 'abc'[1:] == 'bc'
    assert 'abc'[:1] == 'a' # characters from the beginning through and excluding position 1
    assert 'abc'[-1:] == 'c' # characters from the last letter to the end
    assert 'abc'[-2:] == 'bc'
    assert 'abcd'[0:2] + 'abcd'[2:] == 'abcd'
    assert 'abc'[0:99999] == 'abc'
    assert 'abc'[-99999:] == 'abc'
    assert 'abc'[-99999:0] == ''

def test_immutability():
    with pytest.raises(TypeError):
        'abc'[0] = 'd'

def test_length_of_string():
    assert len('abc') == 3
    assert 'abc'.__len__() == 3
    