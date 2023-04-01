import pytest
from decimal import Decimal
from fractions import Fraction

def test_by_default_an_object_is_considered_true():
	assert 5
	assert (4)
	assert {'a': 1}
	class X:
		pass
	assert X()

def test_none_is_considered_false():
	assert not None

def test_false_is_considered_false():
	assert not False

def test_empty_list_is_considered_false():
	assert not []

def test_zero_is_considered_false():
	assert not 0
	assert not 0.0
	assert not 0j
	assert not Decimal(0)
	assert not Fraction(0,1)

def test_an_empty_anything_is_considered_false():
	assert not ""
	assert not ()
	assert not []
	assert not {}
	assert not set()
	assert not range(0)

def test_anything_that_implements_bool_that_returns_false_is_false():
	class X:
		def __bool__(self): 
			return False
	assert not X()

def test_anything_that_implements_len_that_returns_0_is_false():
	class Collection:
		def __len__(self):
			return 0
	assert not Collection()
	