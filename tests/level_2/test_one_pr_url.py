from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__valid():
    assert is_github_pull_request_url(
        "https://github.com/user/repo/pull/1"
    ) is True


def test__is_github_pull_request_url__invalid_domain():
    assert is_github_pull_request_url(
        "https://gitlab.com/user/repo/pull/1"
    ) is False


def test__is_github_pull_request_url__invalid_path():
    assert is_github_pull_request_url(
        "https://github.com/user/repo/issues/1"
    ) is False


def test__is_github_pull_request_url__missing_pull_number():
    assert is_github_pull_request_url(
        "https://github.com/user/repo/pull"
    ) is False


def test__is_github_pull_request_url__extra_path_elements():
    assert is_github_pull_request_url(
        "https://github.com/user/repo/pull/1/files"
    ) is False
