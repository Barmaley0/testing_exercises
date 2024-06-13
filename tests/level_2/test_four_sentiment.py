import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


sentiment_good = {"love", "happy", "joi"}
sentiment_bad = {"hate", "sad", "angry"}


@pytest.mark.parametrize(
    "text,good_words,bad_words,result",
    [
        # check tweet sentiment good
        ("I love this day", sentiment_good, sentiment_bad, "GOOD"),
        # check tweet sentiment bad
        ("I hate this day", sentiment_good, sentiment_bad, "BAD"),
        # check tweet sentiment neutral
        ("I am here", sentiment_good, sentiment_bad, None),
        # check tweet sentiment equal good and bad
        ("I love and hate this day", sentiment_good, sentiment_bad, None),
        # check tweet sentiment multiple good
        ("I love this happy day", sentiment_good, sentiment_bad, "GOOD"),
        # check tweet sentiment multiple bad
        ("I hate this sad day", sentiment_good, sentiment_bad, "BAD"),
        # check tweet sentiment more good
        (
            "I hate this day tomorrow will be happy and more joi",
            sentiment_good,
            sentiment_bad,
            "GOOD",
        ),
        # check tweet sentiment more bad
        (
            "I love this day tomorrow will be sad and angry",
            sentiment_good,
            sentiment_bad,
            "BAD",
        ),
    ],
)
def test__check_tweet_sentiment(text, good_words, bad_words, result):
    assert check_tweet_sentiment(text, good_words, bad_words) is result
