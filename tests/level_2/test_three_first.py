import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize(
    "items,default,result",
    [
        # non empty list
        ([1, 2, 3], None, 1),
        # empty list with default
        ([], 0, 0),
        # empty list with default none
        ([], None, None),
        # list with one element
        ([1], None, 1),
        # list with negative numbers
        ([-1, -2, -3], None, -1),
    ],
)
def test__three_first(items, default, result):
    assert first(items, default) is result
