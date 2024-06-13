import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    "text,replace_from,replace_to,result",
    [
        ("Hello world", "world", "univercse", "Hello univercse"),
        ("Hello Bob", "world", "univercse", "Hello Bob"),
        (
            "Hello World welcome to the world",
            "world",
            "univercse",
            "Hello univercse welcome to the univercse",
        ),
        ("", "world", "univercse", ""),
        ("Hello univercse", "world", "univercse", "Hello univercse"),
    ],
)
def test__five_replace_word__same_case(text, replace_from, replace_to, result):
    assert replace_word(text, replace_from, replace_to) == result
