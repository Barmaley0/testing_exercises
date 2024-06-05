import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
    "square_coefficient,linear_coefficient,const_coefficient,result",
    [
        # two square equation no solution
        (1, 2, 3, (None, None)),
        # two square equation zero square coefficient one solution
        (0, 1, 2, (-2, None)),
        # two square equation zero square and linear coefficient
        (0, 0, -4, (None, None)),
    ],
)
def test__two_square_equation(square_coefficient, linear_coefficient, const_coefficient, result):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == result
