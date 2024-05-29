from datetime import datetime
from decimal import Decimal
from functions.level_1.four_bank_parser import (
    BankCard,
    SmsMessage,
    Expense,
    parse_ineco_expense,
)


def test_parse_ineco_expense():
    # Можно использовать переменные в тесте? Или это плохой пример?
    sms = SmsMessage(
        text="-10.00 RU, 1234 25.05.2024 10:30 MOSCOW RU",
        author="BOBRBANK",
        sent_at=datetime(2024, 5, 25, 10, 30),
    )

    cards = [BankCard(last_digits="1234", owner="Bob Marley")]
    expense = parse_ineco_expense(sms, cards)
    assert expense == Expense(
        amount=Decimal("-10.00"),
        card=BankCard(last_digits="1234", owner="Bob Marley"),
        spent_in="MOSCOW RU",
        spent_at=datetime(2024, 5, 25, 10, 30),
    )
