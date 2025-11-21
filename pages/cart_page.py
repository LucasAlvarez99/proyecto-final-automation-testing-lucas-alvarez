from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def obtener_titulo(self):
        return self.obtener_texto(self.TITLE)

    def ir_a_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
