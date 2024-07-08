import pytest
from datetime import datetime
from functions.level_1.four_bank_parser import BankCard, SmsMessage


@pytest.fixture
def parser_sms_message():
    return SmsMessage(
        text="-20.00 RU, 1234 04.07.2024 22:30 MOSCOW RU",
        author="BOBRBANK",
        sent_at=datetime(2024, 7, 4, 22, 30),
    )


@pytest.fixture
def cards():
    return [BankCard(last_digits="1234", owner="Bob Marley")]
