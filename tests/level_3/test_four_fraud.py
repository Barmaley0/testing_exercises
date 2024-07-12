from functions.level_3.four_fraud import find_fraud_expenses


def test__find_four_fraud(sample_expenses, fraud_expenses):
    assert find_fraud_expenses(sample_expenses) == fraud_expenses
