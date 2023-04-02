import pytest

def test_instantiation():
    a = [1,2,3]
    assert a == [1,2,3]

def test_indexing():
    a = [1,2,3]
    assert a[0] == 1
    assert a[-1] == 3
    assert a[-2] == 2
    assert a[1] == 2

def test_indexing_out_of_range_throws():
    a = [1,2,3]
    with pytest.raises(IndexError):
        assert a[4] == 3
    with pytest.raises(IndexError):
        assert a[-4] == 3

def test_slicing_is_more_permissive():
    a = [1,2,3]
    assert a[-4:] == [1,2,3]
    assert a[4:0] == []

def test_slicing_can_be_used_to_make_a_shallow_copy():
    a = [1,2,3]
    assert a[:] == [1,2,3]

def test_lists_are_mutable():
    a = [1,2,3]
    a[-1] = 4
    assert a == [1,2,4]

def test_slicing_can_be_assigned_to():
    a = [1,2,3]
    a[-2:0] = [4,5,6]
    assert a == [1,4,5,6,2, 3]

    a = [1,2,3]
    a[:] = [4,5]
    assert a == [4,5]

def test_concatenation():
    a = [1,2]
    b = [3]
    assert a + b == [1,2,3]

def test_append_one_item_with_append():
    a = [1,2]
    a.append(3)
    assert a == [1,2,3]

def test_length():
    assert len([1,2,3]) == 3
    assert [1,2,3].__len__() == 3