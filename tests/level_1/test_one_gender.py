import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize(
    "verb_male,verb_female,gender,result",
    [
        ("he", "she", "male", "he"),
        ("he", "she", "female", "she"),
        ("he", "she", "other", "he"),
    ],
)
def test__genderalize(verb_male, verb_female, gender, result):
    if gender == "other":
        assert genderalize(verb_male, verb_female, gender) is not result
    else:
        assert genderalize(verb_male, verb_female, gender) is result
