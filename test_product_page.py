import time
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.skip()
def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_book_add_in_order()
    # time.sleep(5)
    

@pytest.mark.skip()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.login
@pytest.mark.skip()
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        
    
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        
    
    def test_user_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_book_add_in_order()
        
        



@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    email = str(time.time()) + "@fakemail.org"
    password = str(time.time())
    page.register_new_user(email, password)
    page.should_be_authorized_user()
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_book_add_in_order()
    
    
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_book_add_in_order()
    # time.sleep(5)
    
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.check_basket_page()



@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()