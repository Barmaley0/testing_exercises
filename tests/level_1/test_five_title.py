import pytest

from functions.level_1.five_title import change_copy_item


@pytest.mark.parametrize(
    "title,max_main_item_title_length,result",
    [
        ("Test title", 100, "Copy of Test title"),
        (
            "This is a very long name and should not be changed. Therefore, we will leave it as is and test our code to ensure correct execution",
            100,
            "This is a very long name and should not be changed. Therefore, we will leave it as is and test our code to ensure correct execution",
        ),
        ("Copy of test title", 100, "Copy of test title (2)"),
        ("Copy of test title (1)", 100, "Copy of test title (2)"),
        (
            "Copy of This is a very long name and should not be changed. Therefore, we will leave it as is and test our code to ensure correct execution (1)",
            100,
            "Copy of This is a very long name and should not be changed. Therefore, we will leave it as is and test our code to ensure correct execution (1)",
        ),
    ],
)
def test__change_copy_item(title, max_main_item_title_length, result):
    assert change_copy_item(title, max_main_item_title_length) == result
