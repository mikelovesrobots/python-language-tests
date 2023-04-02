import pytest

def test_given_end_point_is_never_part_of_the_sequence():
    assert list(range(3)) == [0,1,2]
    assert list(range(3,3)) == []
    assert list(range(3,4)) == [3]
    assert list(range(3,6,2)) == [3,5]