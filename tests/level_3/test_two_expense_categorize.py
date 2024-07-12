from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category


def test__guess_expense_category(sample_expenses):
    assert guess_expense_category(sample_expenses[0]) == ExpenseCategory.TRANSPORT
    assert guess_expense_category(sample_expenses[1]) == ExpenseCategory.MEDICINE_PHARMACY
    assert guess_expense_category(sample_expenses[2]) == ExpenseCategory.THEATRES_MOVIES_CULTURE
    assert guess_expense_category(sample_expenses[3]) == ExpenseCategory.BAR_RESTAURANT
    assert guess_expense_category(sample_expenses[4]) == ExpenseCategory.ONLINE_SUBSCRIPTIONS
