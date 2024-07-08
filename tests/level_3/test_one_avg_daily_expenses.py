from decimal import Decimal

from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses(sample_expenses):
    average_daily_expanses = calculate_average_daily_expenses(sample_expenses)
    assert average_daily_expanses.quantize(Decimal("0")) == Decimal("7000")
