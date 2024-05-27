import datetime
from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    today = datetime.date.today()
    assert compose_datetime_from(str(today), "15:00") == datetime.datetime(today.year, today.month, today.day, 15, 00)

    tomorrow = today + datetime.timedelta(days=1)
    assert compose_datetime_from("tomorrow", "15:30") == datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 15, 30)
