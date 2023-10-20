from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def check_basket_page(self):
        self.should_be_basket_url()
        self.should_be_empty_basket()
        self.should_be_text_about_empty_basket()
    
    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, 'Url incorrect'
    
    
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET),  'Basket is not empty'
        
        
        
    def should_be_text_about_empty_basket(self):
         assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET), 'No text about empty basket'