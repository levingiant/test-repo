
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


def search_bar(app):
    return app.find_element_by_id("search")


def search_button(app):
    return app.find_element_by_xpath(xpath="//button[@class='button search-button']")


def shirt(app):
    return app.find_element_by_xpath(xpath="(//a[@title='Slim fit Dobby Oxford Shirt'])[2]")


def color_dropdown(app):
    return app.find_element_by_id("attribute92")


def color_option(app):
    return app.find_element_by_xpath(xpath="//option[@value='27']")


def size_dropdown(app):
    return app.find_element_by_id("attribute180")


def size_option(app):
    return app.find_element_by_xpath(xpath="//option[@value='77']")


def add_to_cart(app):
    return app.find_element_by_xpath(xpath="(//button[@title='Add to Cart'])[2]")


def cart_item(app):
    return app.find_element_by_xpath(xpath="//tr[@class='first last odd']")


# Functions


def failed_login(params, app):
    """
    Failed login test.
    :param params: Inputs from user
    :param app:
    :return:
    """
    if params['host'] is None:
        url = "http://www.ctqatest.biz/ecom/customer/account/login/"
    else:
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
    if params['host'] is None:
        url = "http://www.ctqatest.biz/ecom/customer/account/login/"
    else:
        url = params['host']
    app.get(url)
    login_button(app).click()
    if failed_username_validation(app) and failed_password_validation(app):
        return True


def search_shirt(params, app):
    """
    Failed login test.
    :param params: Inputs from user
    :param app:
    :return:
    """
    if params['host'] is None:
        url = "http://www.ctqatest.biz/ecom/customer/account/login/"
    else:
        url = params['host']
    app.get(url)
    search_bar(app).send_keys("shirt")
    search_button(app).click()
    shirt(app).click()
    color_dropdown(app).click()
    color_option(app).click()
    size_dropdown(app).click()
    size_option(app).click()
    add_to_cart(app).click()
    if app.current_url == "http://www.ctqatest.biz/ecom/checkout/cart/":
        if cart_item(app):
            return True
