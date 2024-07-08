from datetime import datetime
from decimal import Decimal

from functions.level_1.four_bank_parser import (
    BankCard,
    Expense,
    parse_ineco_expense,
)


def test__parse_ineco_expense(parser_sms_message, cards):
    expense = parse_ineco_expense(parser_sms_message, cards)
    assert expense == Expense(
        amount=Decimal("-20.00"),
        card=BankCard(last_digits="1234", owner="Bob Marley"),
        spent_in="MOSCOW RU",
        spent_at=datetime(2024, 7, 4, 22, 30),
    )
