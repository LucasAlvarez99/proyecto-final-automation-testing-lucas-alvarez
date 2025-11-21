from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    TITLE = (By.CSS_SELECTOR, ".title")
    CHECKOUT_BTN = (By.ID, "checkout")

    def is_page_loaded(self):
        return self.is_visible(self.TITLE)

    def checkout(self):
        self.click(self.CHECKOUT_BTN)
