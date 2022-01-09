from re import sub
from decimal import Decimal


# Elements
def sales_menu(app):
    return app.find_element_by_xpath(xpath="//li[@class='level0 nav-5 parent']")


def view_all_button(app):
    return app.find_element_by_xpath(xpath="(//a[@class='level1'])[5]")


def price_filter(app):
    return app.find_element_by_xpath(xpath="(//span[@class='price'])[1]")


def price(app):
    return app.find_element_by_xpath(xpath="//span[@class='price']")


# Functions
def sales(params, app, actions_chains):
    if params['host'] is None:
        url = "http://www.ctqatest.biz/ecom/"
    else:
        url = params['host']
    app.get(url)
    actions_chains.move_to_element(sales_menu(app)).perform()
    view_all_button(app).click()
    app.execute_script("arguments[0].scrollIntoView();", price_filter(app))
    price_filter(app).click()

    if Decimal(sub(r'[^\d.]', '', price(app).text)) in range(100, 199):
        return True
