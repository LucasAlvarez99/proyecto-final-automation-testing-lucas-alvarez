from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):

    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def success_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def is_order_complete(self):
        return self.is_visible(self.COMPLETE_HEADER)
