from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url("sberbank.ru", "page1") == "sberbank.ru/page1"
    assert build_url("sberbank.ru", "page1", {"param1": "value1"}) == "sberbank.ru/page1?param1=value1"
    assert build_url("sberbank.ru", "page1", {"param1": "value1", "param2": "value2"}) == "sberbank.ru/page1?param1=value1&param2=value2"
    assert build_url("sberbank.ru", "page1", {"param1": "value+with+space", "param2": "value%20with%20urlencoding"}) == "sberbank.ru/page1?param1=value+with+space&param2=value%20with%20urlencoding"
