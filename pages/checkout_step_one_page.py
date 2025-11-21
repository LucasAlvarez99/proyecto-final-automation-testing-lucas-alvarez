from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def fill_form(self, first, last, zip_code):
        self.send_keys(self.FIRST_NAME, first)
        self.send_keys(self.LAST_NAME, last)
        self.send_keys(self.ZIP, zip_code)

    def continue_to_step_two(self):
        self.click(self.CONTINUE_BTN)
