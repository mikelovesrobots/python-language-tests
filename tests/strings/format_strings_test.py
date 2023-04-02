import pytest

def test_format():
    assert "Here is my parameters: {} and {}".format(1,2) == "Here is my parameters: 1 and 2"

def test_positional_arguments():
    assert '{2}, {1}, {0}'.format('a', 'b', 'c') == 'c, b, a'

def test_keyword_arguments():
    assert 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W') == 'Coordinates: 37.24N, -115.81W'
    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    assert 'Coordinates: {latitude}, {longitude}'.format(**coord) == 'Coordinates: 37.24N, -115.81W'

def test_format_commas():
    assert '{:,}'.format(1234567890) == '1,234,567,890'

def test_format_percentages():
    assert '{:.2%}'.format(.3456) == '34.56%'

def test_accessing_arguments_items():
    coord = (3, 5)
    assert 'X: {0[0]};  Y: {0[1]}'.format(coord) == 'X: 3;  Y: 5'

def test_alignment():
    assert '{:<6}'.format(1.23) == '1.23  '
    assert '{:>6}'.format(1.23) == '  1.23'
    assert '{:^6}'.format(1.23) == ' 1.23 '
    assert '{:*>6}'.format(1.23) == '**1.23' # use * as a fill char
