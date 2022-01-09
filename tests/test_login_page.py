from test_repo.lib.ui.login_page import failed_login


def test_failed_login(params, app):
    """
    Login test for wallashops
    :param params:
    :return:
    """
    msg = 'There was an issue logging in'
    assert failed_login(params, app), msg
