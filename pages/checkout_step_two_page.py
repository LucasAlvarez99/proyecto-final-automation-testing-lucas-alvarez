from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutStepTwoPage(BasePage):

    FINISH_BUTTON = (By.ID, "finish")

    def finalizar(self):
        self.click(self.FINISH_BUTTON)
