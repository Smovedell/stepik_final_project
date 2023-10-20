from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Current url not correct'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.ENTER_EMAIL), 'Not found email form in login form'
        assert self.is_element_present(*LoginPageLocators.ENTER_PASS), 'Not found password form in login form'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), 'Not found email form in registration form'
        assert self.is_element_present(*LoginPageLocators.REG_PASS), 'Not found password form in registration form'
        assert self.is_element_present(*LoginPageLocators.REG_PASS_2), 'Not found password2 form in registration form'
        
    def register_new_user(self, email, password):
        self.should_be_login_page()
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()