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
