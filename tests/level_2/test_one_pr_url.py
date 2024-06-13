import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(
    "url,result",
    [
        # url valid
        (
            "https://gitlab.com/user/repo/pull/1",
            False,
        ),
        # url invalid domain
        (
            "https://gitlab.com/user/repo/pull/1",
            False,
        ),
        # url invalid path
        (
            "https://github.com/user/repo/issues/1",
            False,
        ),
        # missing pull number
        (
            "https://github.com/user/repo/pull",
            False,
        ),
        # extra path elements
        (
            "https://github.com/user/repo/pull/1/files",
            False,
        ),
    ],
)
def test__is_github_pull_request_url(url, result):
    assert is_github_pull_request_url(url) is result
