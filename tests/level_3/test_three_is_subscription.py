
from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription(sample_expenses):
    expense = sample_expenses[0]
    history = sample_expenses[:3]
    assert is_subscription(expense, history) is False

    expense = sample_expenses[0]
    history = sample_expenses
    assert is_subscription(expense, history) is False
