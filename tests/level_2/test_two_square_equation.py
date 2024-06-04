from functions.level_2.two_square_equation import solve_square_equation


def test__two_square_equation_no_solution():
    assert solve_square_equation(1, 2, 3) == (None, None)


def test__two_square_equation_zero_square_coefficient_one_solutions():
    assert solve_square_equation(0, 1, 2) == (-2, None)


def test__two_square_equation_zero_square_and_linear_coefficients():
    assert solve_square_equation(0, 0, -4) == (None, None)
