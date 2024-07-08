import pytest
from datetime import datetime
from decimal import Decimal

from functions.level_3.four_fraud import find_fraud_expenses
from functions.level_3.models import Expense, BankCard, ExpenseCategory, Currency


@pytest.fixture
def sample_expenses() -> list[Expense]:
    return [
        Expense(
            amount=Decimal("1000.00"),
            currency=Currency.RUB,
            card=BankCard(last_digits="1234", owner="Bob Marley"),
            spent_in="gg platform",
            spent_at=datetime(2010, 1, 1),
            category=ExpenseCategory.TRANSPORT,
        ),
        Expense(
            amount=Decimal("2000.00"),
            currency=Currency.EUR,
            card=BankCard(last_digits="0345", owner="bart simpson"),
            spent_in="pharm",
            spent_at=datetime(2024, 7, 4, 22, 30),
            category=ExpenseCategory.MEDICINE_PHARMACY,
        ),
        Expense(
            amount=Decimal("3000.00"),
            currency=Currency.USD,
            card=BankCard(last_digits="5678", owner="lisa simpson"),
            spent_in="cinema galleria",
            spent_at=datetime(2024, 7, 4, 10, 29),
            category=ExpenseCategory.THEATRES_MOVIES_CULTURE,
        ),
        Expense(
            amount=Decimal("4000.00"),
            currency=Currency.USD,
            card=BankCard(last_digits="9012", owner="homer simpson"),
            spent_in="doc",
            spent_at=datetime(2024, 10, 5, 15, 30),
            category=ExpenseCategory.BAR_RESTAURANT,
        ),
        Expense(
            amount=Decimal("5000.00"),
            currency=Currency.USD,
            card=BankCard(last_digits="3456", owner="marge simpson"),
            spent_in="apple.com/bill",
            spent_at=datetime(2024, 7, 4, 10, 29),
            category=ExpenseCategory.ONLINE_SUBSCRIPTIONS,
        ),
        Expense(
            amount=Decimal("6000.00"),
            currency=Currency.USD,
            card=BankCard(last_digits="7890", owner="marge simpson"),
            spent_in="cinema galleria",
            spent_at=datetime(2024, 7, 4, 10, 29),
            category=ExpenseCategory.THEATRES_MOVIES_CULTURE,
        ),
    ]


@pytest.fixture
def fraud_expenses(sample_expenses):
    return find_fraud_expenses(sample_expenses)
