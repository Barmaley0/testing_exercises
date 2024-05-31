from functions.level_2.five_replace_word import replace_word


def test__five_replace_word__same_case():
    assert replace_word("Hello world", "world", "univercse") == "Hello univercse"


def test__five_replace_word__different_case():
    assert replace_word("Hello Bob", "world", "univercse") == "Hello Bob"


def test__five_replace_word__multiple_instances():
    assert (
        replace_word("Hello World welcome to the world", "world",
                     "univercse") == "Hello univercse welcome to the univercse"
    )


def tets__five_replace_word__empty_string():
    assert replace_word("", "world", "univercse") == ""


def test__five_replace_word__no_match():
    assert replace_word("Hello univercse", "world", "univercse") == "Hello univercse"
