from selenium.webdriver import ActionChains


# Elements

def email_textbox(app):
    return app.find_element_by_xpath(xpath="//input[@type='email']")


def pass_textbox(app):
    return app.find_element_by_xpath(xpath="//input[@type='password']")


def failed_login_message(app):
    return app.find_element_by_xpath(xpath="//span[.='Invalid login or password.']")


def login_button(app):
    return app.find_element_by_xpath("//button[@id='send2']")


def failed_username_validation(app):
    return app.find_element_by_id("advice-required-entry-email")


def failed_password_validation(app):
    return app.find_element_by_id("advice-required-entry-pass")


# Functions


def failed_login(params, app):
    """
    Failed login test.
    :param params: Inputs from user
    :param driver:
    :return:
    """
    url = params['host']
    app.get(url)
    email_textbox(app).send_keys(params["username"])
    pass_textbox(app).send_keys(params["password"])
    login_button(app).click()
    app.implicitly_wait(10)

    if failed_login_message(app):
        return True


def failed_login_validations(params, app):
    """
    Failed login test.
    :param params: Inputs from user
    :param app:
    :return:
    """
    url = params['host']
    app.get(url)
    login_button(app).click()
    if failed_username_validation(app) and failed_password_validation(app):
        return True
