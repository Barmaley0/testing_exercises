from functions.level_2.four_sentiment import check_tweet_sentiment


sentiment_good = {"love", "happy", "joi"}
sentiment_bad = {"hate", "sad", "angry"}


def test__check_tweet_sentiment__sentiment_good():
    result = check_tweet_sentiment("I love this day", sentiment_good, sentiment_bad)
    assert result == "GOOD"


def test__check_tweet_sentiment__sentiment_bad():
    result = check_tweet_sentiment("I hate this day", sentiment_good, sentiment_bad)
    assert result == "BAD"


def test__check_tweet_sentiment__sentiment_neutral():
    result = check_tweet_sentiment("I am here", sentiment_good, sentiment_bad)
    assert result is None


def test__check_tweet_sentiment__sentiment_equal_good_bad():
    result = check_tweet_sentiment("I love and hate this day", sentiment_good, sentiment_bad)
    assert result is None


def test__check_tweet_sentiment__sentiment_multiple_good():
    result = check_tweet_sentiment("I love this happy day", sentiment_good, sentiment_bad)
    assert result == "GOOD"


def test__check_tweet_sentiment__sentiment_multiple_bad():
    result = check_tweet_sentiment("I hate this sad day", sentiment_good, sentiment_bad)
    assert result == "BAD"


def test__check_tweet_sentiment__sentiment_more_good():
    result = check_tweet_sentiment(
        "I hate this day tomorrow will be happy and more joi",
        sentiment_good, sentiment_bad)
    assert result == "GOOD"


def test__check_tweet_sentiment__sentiment_more_bad():
    result = check_tweet_sentiment(
        "I love this day tomorrow will be sad and angry",
        sentiment_good, sentiment_bad)
    assert result == "BAD"
