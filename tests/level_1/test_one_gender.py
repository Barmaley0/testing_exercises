from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize("he", "she", "male") == "he"
    assert genderalize("he", "she", "female") == "she"
    assert not genderalize("he", "she", "other") == "he"
