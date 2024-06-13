import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    "host_name,relative_url,get_params,result",
    [
        ("sberbank.ru", "page1", "", "sberbank.ru/page1"),
        (
            "sberbank.ru",
            "page1",
            {"param1": "value1"},
            "sberbank.ru/page1?param1=value1",
        ),
        (
            "sberbank.ru",
            "page1",
            {"param1": "value1", "param2": "value2"},
            "sberbank.ru/page1?param1=value1&param2=value2",
        ),
        (
            "sberbank.ru",
            "page1",
            {"param1": "value+with+space", "param2": "value%20with%20urlencoding"},
            "sberbank.ru/page1?param1=value+with+space&param2=value%20with%20urlencoding",
        ),
    ],
)
def test__build_url(host_name, relative_url, get_params, result):
    if get_params == "":
        assert build_url(host_name, relative_url) == result
    else:
        assert build_url(host_name, relative_url, get_params) == result
