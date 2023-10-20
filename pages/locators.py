from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators():
    ENTER_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    ENTER_PASS = (By.CSS_SELECTOR, "#id_login-password")
    
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form button")
    
    
class ProductPageLocators():
    ORDER_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_FORM = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    COST_FORM = (By.CSS_SELECTOR, '.alert-info p strong')
    BOOK_NAME_IN_HEAD = (By.CSS_SELECTOR, '.product_main h1')
    COST_IN_HEAD = (By.CSS_SELECTOR, '.product_main .price_color')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini>span')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR,'#content_inner>p>a')
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, '.basket-title')