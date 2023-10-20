from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def should_be_book_add_in_order(self):
        self.should_be_order_button()
        self.add_book()
        try:
            self.solve_quiz_and_get_code()
        except:
            pass
        self.should_be_name()
        self.should_be_similar_name()
        self.should_be_cost()
        self.should_be_similar_cost()
    
    def should_be_similar_name(self):
        name_in_order = self.browser.find_element(*ProductPageLocators.NAME_FORM).text
        main_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_HEAD).text
        assert main_name == name_in_order, "Names are different"
    
    def should_be_similar_cost(self):
        cost_in_order = self.browser.find_element(*ProductPageLocators.COST_FORM).text
        main_cost = self.browser.find_element(*ProductPageLocators.COST_IN_HEAD).text
        assert cost_in_order == main_cost, "Costs are different"
    
    def add_book(self):
        button = self.browser.find_element(*ProductPageLocators.ORDER_BUTTON)
        button.click()
        
    def should_be_order_button(self):
        assert self.is_element_present(*ProductPageLocators.ORDER_BUTTON), "Order button not found"
        
    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.NAME_FORM), "Name form not found"
    
    def should_be_cost(self):
        assert self.is_element_present(*ProductPageLocators.COST_FORM), "Cost form not found"
        
        
    def should_not_be_name_after_adding(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_FORM)
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_FORM)
    
    def should_disappeared_after_adding(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_FORM)