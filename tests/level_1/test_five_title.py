from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item("Test title", 100) == "Copy of Test title"
    assert change_copy_item("This is a very long name and should not be changed. Therefore, we will leave it as is and test our code to ensure correct execution", 100) == "This is a very long name and should not be changed. Therefore, we will leave it as is and test our code to ensure correct execution"
    assert change_copy_item("Copy of test title", 100) == "Copy of test title (2)"
    assert change_copy_item("Copy of test title (1)", 100) == "Copy of test title (2)"
    assert change_copy_item("Copy of This is a very long name and should not be changed. Therefore, we will leave it as is and test our code to ensure correct execution (1)", 100) == "Copy of This is a very long name and should not be changed. Therefore, we will leave it as is and test our code to ensure correct execution (1)"
