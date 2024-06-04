import pytest
from functions.level_2.three_first import first


def test__three_first__non_empty_list():
    assert first([1, 2, 3]) == 1


def test__three_first__empty_list_with_default():
    assert first([], default=0) == 0


def test__three_first__empty_list_with_default_none():
    assert first([], default=None) is None


def test__three_first__list_with_one_element():
    assert first([1]) == 1


def test__three_first__list_with_negative_numbers():
    assert first([-1, -2, -3]) == -1


def test__three_first__empty_list_with_default_none_set():
    with pytest.raises(AttributeError):
        first([])
