from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest



link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
timeout = 0

@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout)
    page.open()
    page.add_book()
    page.should_not_be_name_after_adding()

    


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, timeout)
    page.open()
    page.should_not_be_success_message()

    


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout)
    page.open()
    page.add_book()
    page.should_disappeared_after_adding()
