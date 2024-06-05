import datetime
import pytest

from functions.level_1.two_date_parser import compose_datetime_from


today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)


@pytest.mark.parametrize(
    "date_str,time_str,result",
    [
        (
            str(today),
            "15:00",
            datetime.datetime(today.year, today.month, today.day, 15, 00),
        ),
        (
            "tomorrow",
            "15:30",
            datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 15, 30),
        ),
    ],
)
def test__compose_datetime_from(date_str, time_str, result):
    assert compose_datetime_from(date_str, time_str) == result
