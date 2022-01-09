from test_repo.lib.ui.home_page import sales


def test_sale_filter(params, app, actions_chains):
    """
    Login test.
    :param params:
    :return:
    """
    msg = 'There was an issue logging in'
    assert sales(params, app, actions_chains), msg
