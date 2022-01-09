from test_repo.lib.ui.login_page import failed_login, failed_login_validations, search_shirt


def test_failed_login(params, app):
    """
    Login test.
    :param params:
    :return:
    """
    msg = 'There was an issue logging in'
    assert failed_login(params, app), msg


def test_failed_login_validations(params, app):
    """
    Login test.
    :param params:
    :return:
    """
    msg = 'There was an issue logging in'
    assert failed_login_validations(params, app), msg


def test_search_shirt(params, app):
    """
    Login test.
    :param params:
    :return:
    """
    msg = 'There was an issue logging in'
    assert search_shirt(params, app), msg
