from functools import reduce
import pytest

def test_iterating_with_built_in_counter():
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for counter, value in enumerate(my_list):
        counter, value
    assert counter == 3

def test_iterating_with_enumerate_and_starting_indices():
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for counter, value in enumerate(my_list, 1):
        counter, value
    assert counter == 4

def test_iterating_over_multiple_lists_at_the_same_time():
    a = ['apple', 'banana', 'grapes']
    b = [5,10,15]
    c = ['a','b','c']
    for fruit, number, letter in zip(a, b, c):
        pass
    assert fruit == 'grapes'
    assert number == 15
    assert letter == 'c'

def test_map():
    a = list(map(lambda x: x + 1, [1,2,3]))
    assert a == [2,3,4]

def test_filter():
    a = list(filter(lambda x: x > 1, [1,2,3]))
    assert a == [2,3]

def test_reduce_without_reduce():
    product = 1
    list = [1, 2, 3, 4]
    for num in list:
        product = product * num
    assert product == 24

def test_reduce_with_reduce():
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    assert product == 24

def test_iterating_over_a_dict():
    a = {"a": 1}
    b = {}
    for k, v in a.items():
        b[k] = v
    assert b == a

def test_iterating_n_times():
    a = 0
    for x in range(5):
        a += 1
    assert a == 5

def test_iterating_over_indices():
    a = [1,2,3]
    b = 0
    for i in range(len(a)):
        b += a[i]
    assert b == 6